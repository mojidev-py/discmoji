from typing import *
import aiohttp
import asyncio
from .types import Payload,OPCODES,initiatelogging,formatter,AppInfo
from random import uniform
import os
from ._http import EndpointManager
from .errors import DiscmojiAPIError




class GatewayManager:
    def __init__(self,token: str,intents: int,endpointclient: EndpointManager):
        # handles the gateway connections/events and turns recieved payloads into the Payload object for easier use
        self.token = token
        self.intents = intents
        self.ws_url = asyncio.run(endpointclient.send_request(method="get",route="/gateway")).data["url"]
        self.client = aiohttp.ClientSession()
        self.ws = self.client.ws_connect(self.url)
        self.HB_INT: int | None = None
        self.current_payload: Payload | None = None
        self.guild_count: int | None = None
        self.captured_app_info: None | AppInfo = None
        self.session_id: None | str | int = None
        self.resume_url: None | str = None 
        self.current_seq: int | None = None
        
    
    async def _abstractor(self) -> Payload:  
        # "abstracts" the recieved str payload into a Payload object it can use to do some extra logic without having to listen for a specific opcode or event name through ugly
        # dict keys ;_;
        async with self.ws as ws:
            serialized = await ws.receive_json()
            payloaded = Payload(serialized["op"],serialized["d"],serialized["t"],serialized["s"])
            self.current_payload = payloaded
            return payloaded
    
    async def _handle_heartbeats(self):
        # as the func title says, handles the heartbeats of the gateway
        # captures the event before starting the heartbeat so it can send the corresponding sequence num
        event = await self._abstractor()
        jsonized = None
        if event.code == OPCODES.EVENT:
            payload = Payload(code=OPCODES.HEARTBEAT,d=event.seq)
            jsonized = payload.jsonize()
            self.current_seq = event.seq
        else:
            # if it didn't recieve any event from the abstractor func, it sends no data, just opcode 1.
            payload = Payload(code=1,d=None)
            jsonized = payload.jsonize()
        async with self.ws as ws:
          if event.code == OPCODES.HELLO:  
            # handles the heartbeat if it's the first one
            await asyncio.sleep(float(self.HB_INT)*uniform(float(0),float(1)))
          else:
            await asyncio.sleep(float(self.HB_INT))   
            await ws.send_str(data=jsonized)
            # captures the next event 
            await self._abstractor()


            
    
    async def _hand_shake(self):
        # handles the initial connection process
        async with self.ws as ws:
            hb_int = await self._abstractor()
            self.HB_INT = hb_int.data
            initiatelogging.info(f"Recieved HELLO event. Initating heartbeat at {self.HB_INT / 1000.:2f} seconds.")
            firstpayload = Payload(code=OPCODES.IDENTIFY,d={
                "token":self.token,
                "properties": {
                    "os": "windows" if os.name == "nt" else "linux",
                    "browser": "discmoji",
                    "device": "discmoji"
                },
                # the sharding field will be handled in ShardedGatewayManager (presence isn't implemented yet)
                "intents": self.intents
            })
            jsonized = firstpayload.jsonize()
            await ws.send_str(jsonized)
            capture_guild_count = await self._abstractor() 
            if capture_guild_count.code is None:
                self.guild_count = len(capture_guild_count.data["guilds"])
                initiatelogging.info(f"Recieved READY event. Connected to gateway at session id: {capture_guild_count.data["session_id"]}, as {capture_guild_count.data["application"]["bot"]["username"]}#{capture_guild_count.data["application"]["bot"]["discriminator"]}")
                self.captured_app_info: AppInfo = AppInfo(capture_guild_count.data["application"])
                self.session_id = capture_guild_count.data["session_id"]
    
    async def _reconnect_with_data(self):
        if self.current_payload.code == OPCODES.RECONNECT:
            initiatelogging.info("Gateway sent a RECONNECT event. Initiating reconnect process . . .")
            self.client = aiohttp.ClientSession()
            self.ws = self.client.ws_connect(self.resume_url)
            async with self.ws as ws:    
             try:   
                sending = Payload(code=6,d={
                    "token": self.token,
                    "session_id": self.session_id,
                    "seq": self.current_seq
                })
                jsonized = sending.jsonize()
                sent = await ws.send_str(jsonized)
                response = await ws.receive_json()
                if response == OPCODES.RESUME:
                    initiatelogging.info("Successfully reconnected to gateway using new url.")
             except aiohttp.ClientError as e:
                 raise DiscmojiAPIError(f"Discmoji couldn't reconnect to the gateway. {e.args}. raw payload:{self.current_payload.data}")
        
    async def handle_gateway_event(self, event_name: str, callback: Callable[[Payload], Awaitable[None]]):
        while True:
            event = await self._abstractor()
            if event.event_name == event_name:
                await callback(event)

    async def handle_all_gateway_events(self, callback: Callable[[Payload], Awaitable[None]]):
        while True:
            event = await self._abstractor()
            await callback(event)
