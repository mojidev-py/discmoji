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
from ._http import HttpManager
import asyncio
from .intents import BotIntents
import websockets
from .types import WebsocketPayload,Opcodes,logger
from contextlib import asynccontextmanager
from typing import Self
from random import uniform
import json

class DiscordWebsocket:
    def __init__(self,http: HttpManager,intents: BotIntents):
        self.ws = None
        self.token = http.token
        self.intents = intents._deconv_intents()
        self.interval: int = None
        self.seq: int | None = None 
        self.url: str = None
    
    @asynccontextmanager
    # huge credit to graingert on discord!
    async def initiate_connection(cls,ws: websockets.WebSocketClientProtocol,http: HttpManager,intents: BotIntents):
        url = await http.request('get','/gateway/bot',True).data["url"]
        async with websockets.connect(url) as ws:
                cls.ws = ws
                try:
                    goingtobeyield: Self = cls(ws,http,intents)
                    yield goingtobeyield
                except websockets.ConnectionClosedError:
                    raise RuntimeError("Gateway closed connection.")
                    
    
    async def _recieve_latest(self):
        result: dict = json.loads(await self.ws.recv())
        self.seq = result.get("s")
        # .get because sequence field may be none at times
        return WebsocketPayload(opcode=result["op"],data=result["d"])

    async def first_heart_beat(self):
        msg = WebsocketPayload(opcode=Opcodes.HEARTBEAT,data=None)
        await self.ws.send(msg.jsonize())
    
    async def resume(self):
        msg = WebsocketPayload(opcode=Opcodes.RESUME,data={
            "token": self.token,
            "session_id": self.url,
            "seq": self.seq
        })
        await self.ws.send(msg.jsonize())
        recv: dict = json.loads(await self.ws.recv())
        if recv.get("op") != 9:
            logger.info(f"Successfully resumed connection with gateway. Payload: \n {recv}")
        else:
            logger.fatal(f"Invalid Session. Report this to devs with payload! {recv}")
            
    
    async def _heart_beat_loop(self,seq: int):
        while True:
            recv = json.loads(await self.ws.recv())
            logger.info(f"Payload recieved: \n {recv}")
            await asyncio.sleep(self.interval)
            # placed above since no wait during sending reconnect event
            if recv["op"] == Opcodes.RECONNECT:
                await self.resume()
            if recv["op"] == Opcodes.HEARTBEAT:
                send = WebsocketPayload(opcode=recv["op"],data=recv["d"])
                await self.ws.send(send.jsonize())
            msg = WebsocketPayload(opcode=Opcodes.HEARTBEAT,data=seq)
            await self.ws.send(msg.jsonize())
    
    async def _handshake(self):
        recv = await self._recieve_latest()
        if recv.opcode == Opcodes.HELLO:
            self.interval = recv.data["heartbeat_interval"]
            await asyncio.sleep(uniform(0,1))
            await self.first_heart_beat()
            asyncio.create_task(self._heart_beat_loop(self.seq))
        if recv.opcode == Opcodes.ACK:
            logger.info(f"Initiated Heartbeat with gateway at interval of {self.interval / 1000} s.")
        identify = WebsocketPayload(opcode=2,data = {
            "token": self.token,
            "properties": {
                "os": "linux",
                "browser": "discmoji",
                "device": "discmoji"
            },
            "intents": self.intents
        })
        await self.ws.send(identify.jsonize())
        recv = await self._recieve_latest()
        
        if recv.opcode == Opcodes.DISPATCH:
            logger.info(f"Successfully established connection to gateway at session id: {recv.data["session_id"]}")
            logger.info(f"Bot Name: {recv.data["application"]["name"]}")
            self.url = recv.data["resume_gateway_url"]
        
        
            