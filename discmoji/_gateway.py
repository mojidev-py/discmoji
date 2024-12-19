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
SOFTWARE.
"""
from ._types import WebsocketPayload,Opcodes
from .intents import BotIntents
from ._http import HttpManager
import asyncio
import websockets
from contextlib import asynccontextmanager
from typing import Self
from random import uniform
import logging
import json
import sys


logger = logging.getLogger("discmoji")
class DiscordWebsocket:
    def __init__(self,http: HttpManager,intents: BotIntents):
        self.token = http.token
        self.intents = intents._deconv_intents()
    
    @classmethod
    @asynccontextmanager
    # huge credit to graingert on discord!
    async def initiate_connection(cls,http: HttpManager,intents: BotIntents):
        rq = await http.request('get','gateway/bot',True)
        url = f"{rq.data["url"]}/?v=10&encoding=json"
        async with websockets.connect(url) as ws:
                cls.ws = ws
                try:
                    goingtobeyield: Self = cls(http,intents)
                    yield goingtobeyield
                except websockets.ConnectionClosedError as e:
                    raise RuntimeError(f"Gateway closed connection. {e}")
                    
    
    async def send_identify(self):
        payload = WebsocketPayload(None,2,{
            "token": self.token,
            "properties": {
                "os": sys.platform,
                "browser": "discmoji",
                "device": "discmoji"
            },
            "presence": {
                "activities": [{
                    "name": "made using discmoji",
                    "type": 0
                }],
                "status": "online",
                "afk": False
                },
            "intents":self.intents
            })
        await self.ws.send(payload.jsonize())
   
   
   
    async def send_heartbeats(self,delay: int):
        n = 0
        logger.info(f"Initiating heartbeat at interval of {delay}ms.")
        while True:
            await asyncio.sleep(delay / 1000)
            n += 1
            sequence = {
                "seq": self.seq if self.seq else None
            }
            payload = WebsocketPayload(None,1,sequence)
            await self.ws.send(payload.jsonize())
    
    async def resume_session(self):
        payload = WebsocketPayload(None,6,{
            "token": self.token,
            "session_id": self.session_id,
            "seq": self.seq
        })
        
        
    
    async def _establish(self):
        async for message in self.ws:
            logger.debug(f"Recieved Payload: {message}")    
            decoded: dict = json.loads(message)
            self.seq = decoded["s"]
            payloaded = WebsocketPayload(None,decoded["op"],decoded["d"])
            match payloaded.opcode:
                    case 10:
                        await self.send_identify()
                        asyncio.ensure_future(self.send_heartbeats(payloaded.data["heartbeat_interval"]))
                    case 0:
                        if payloaded.data.get("v") is not None:
                            self.session_id = payloaded.data["session_id"]
                            logger.info(f"Established connection to discord gateway at session id: {payloaded.data["session_id"]} \n User: {payloaded.data["user"]["username"]}")      
                
            

            
            
        
        
            