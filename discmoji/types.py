"""MIT License

Copyright (c) 2024 mojidev-py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

from enum import Enum
from typing import *
import json
import aiohttp
import os
import asyncio
from random import uniform


class OPCODES(Enum):
    # internal class that's used for getting opcodes easily without typing the code in manually
    IDENTIFY = 0
    RESUME = 6
    HEARTBEAT = 1
    REQUEST_GUILD_MEMBERS = 8
    UPDATE_VOICE_STATE = 4
    PRESENCE_UPDATE = 3
    HELLO = 10
    RECONNECT = 7
    INVALID = 9
    EVENT = 0
    ACK = 11
    HTTP = None




class Payload:
    def __init__(self,
                 code: int,
                 d: Optional[Dict | str | int],
                 event_name: Optional[str],
                 s: Optional[int]):
        # class used for representing a payload from the api, or to the api
        # event_name attribute handles the event name from the gateway that GatewayManager handles 
        self.code = code
        self.event_name = event_name
        self.data = d
        self.seq = s
        
    def jsonize(self):
        # jsonizes the payload to be sent (websockets lib restrictions)
        jsoned = {
            "op": self.code,
            "d": self.data,
        }
        return json.dumps(jsoned)


class EndpointManager:

    def __init__(self,token: str):
        self.token = token
        self.base_url = "https://discord.com/api"
        # persistent headers, will only use authorization header incase request needs authorization
        self.headers = {"User-Agent":"DiscordBot https://github.com/mojidev-py/discmoji, 0.0.1pr"}
        self.httpclient = aiohttp.ClientSession(base_url=self.base_url,headers=self.headers)
        self.ws_url = None #yet
    
    
    
    async def send_request(self,method: Literal['get','post','put','patch','delete'],route: str) -> Payload:
        # sends a request and returns a payload with the content it recieved back
        async with self.httpclient as client:
            match method:
                case "get":  
                    sent = await client.get(self.url+route)
                    parsed = await sent.read()
                    decoded = await parsed.decode(encoding="utf-8")
                    # return statement returns the decoded and deserialized content that StreamReader recieves
                    return Payload(code=OPCODES.HTTP,d=json.loads(decoded),event_name="HTTP_REQUEST_RECIEVED")
                case "post":
                    pass
                    
                    
        




class GatewayManager:
    def __init__(self,token: str,intents: int,endpointclient: EndpointManager):
        # handles the gateway connections/events and turns recieved payloads into the Payload object for easier use
        self.token = token
        self.intents = intents
        self.ws_url = endpointclient.send_request(method="get",route="/gateway")
        self.client = aiohttp.ClientSession()
        self.ws = self.client.ws_connect(self.url)
        self.HB_INT = None
    
    
    async def _abstractor(self) -> Payload:  
        # "abstracts" the recieved str payload into a Payload object it can use to do some extra logic without having to listen for a specific opcode or event name through ugly
        # dict keys ;_;
        async with self.ws as ws:
            serialized = await ws.receive_json()
            # 
            payloaded = Payload(serialized["op"],serialized["d"],serialized["t"],serialized["s"])
            return payloaded
    
    async def _handle_heartbeats(self):
        # as the func title says, handles the heartbeats of the gateway
        # captures the event before starting the heartbeat so it can send the corresponding sequence num
        event = await self._abstractor()
        jsonized = None
        if event.code == OPCODES.EVENT:
            payload = Payload(code=OPCODES.HEARTBEAT,d=event.seq)
            jsonized = payload.jsonize()
        else:
            # if it didn't recieve any event from the abstractor func, it sends no data, just opcode 1.
            payload = Payload(code=1,d=None)
            jsonized = payload.jsonize()
        async with self.ws as ws:
          if event.code == OPCODES.HELLO:  
            # handles the heartbeat if it's the first one
            asyncio.sleep(float(self.HB_INT)*uniform(float(0),float(1)))
          else:
            asyncio.sleep(float(self.HB_INT))   
            await ws.send_str(data=jsonized)
            # captures the next event 
            await self._abstractor()
            
    
    async def _hand_shake(self):
        # handles the initial connection process
        async with self.ws as ws:
            hb_int = await self._abstractor()
            self.HB_INT = hb_int.data
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
            



        
            