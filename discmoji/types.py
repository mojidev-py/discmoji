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
        self.opcodes = OPCODES
        
    def jsonize(self):
        # jsonizes the payload to be sent (websockets lib restrictions)
        s = "s" if self.code == self.opcodes.HEARTBEAT else  ""
        jsoned = {
            "op": self.code,
            "d": self.data,
            s: self.seq if self.code == self.opcodes.HEARTBEAT else ""
        }
        return json.dumps(jsoned)


class GatewayManager:
    def __init__(self,token: str,intents: int):
        # handles the gateway connections/events and turns recieved payloads into the Payload object for easier use
        self.token = token
        self.intents = intents
        self.url = "wss://gateway.discord.gg/?v=10&encoding=json"
        self.client = aiohttp.ClientSession()
        self.ws = self.client.ws_connect(self.url)
        self.HB_INT = None
    
    
    async def _abstractor(self) -> Payload:  
        # "abstracts" the recieved str payload into a Payload object it can use to do some extra logic without having to listen for a specific opcode or event name through ugly
        # dict keys ;_;
        async with self.ws as ws:
            serialized = await ws.receive_json()
            payloaded = Payload(serialized["op"],serialized["d"],serialized["t"],serialized["s"] if serialized["s"] is not None else None)
            return payloaded
    
    async def _handle_heartbeats(self):
        # as the func title says, handles the heartbeats of the gateway
        event = await self._abstractor()
        jsonized = None
        if event.code == event.opcodes.EVENT:
            payload = Payload(code=1,d=event.seq)
            jsonized = payload.jsonize()
        async with self.ws as ws:
            await ws.send_str(data=jsonized)
            # captures the next event 
            await self._abstractor()
    
    async def _hand_shake(self):
        # handles the initial connection process
        ...

            