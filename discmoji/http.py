from typing import *
import aiohttp
import asyncio
from .types import Payload,OPCODES
import json




class EndpointManager:

    def __init__(self,token: str):
        self.token = token
        self.base_url = "https://discord.com/api/v10"
        # persistent headers, will only use authorization header incase request needs authorization
        self.headers = {"User-Agent":"DiscordBot https://github.com/mojidev-py/discmoji, 0.0.1pr"}
        self.httpclient = aiohttp.ClientSession(base_url=self.base_url,headers=self.headers)#yet
    
    
    
    async def send_request(self,method: Literal['get','post','put','patch','delete'],route: str) -> Payload:
        # sends a request and returns a payload with the content it recieved back
        async with self.httpclient as client:
            match method:
                case "get":  
                    sent = await client.get(self.base_url+route)
                    parsed = await sent.read()
                    decoded = await parsed.decode(encoding="utf-8")
                    # return statement returns the decoded and deserialized content that StreamReader recieves
                    return Payload(code=OPCODES.HTTP,d=json.loads(decoded),event_name="HTTP_REQUEST_RECIEVED")
                case "post":
                    sent = await client.post(url=self.base_url+route)
                    parsed = await sent.read()
                    decoded = await parsed.decode(encoding="utf-8")
                    return Payload(OPCODES.HTTP,d=json.loads(decoded),event_name="HTTP_REQUEST_RECIEVED")
                case "put":
                    sent = await client.put(url=self.base_url+route)
                    parsed = await sent.read()
                    decoded = await parsed.decode()
                    return Payload(OPCODES.HTTP,d=json.loads(decoded),event_name="HTTP_REQUEST_RECIEVED")
                case "patch":
                    sent = await client.patch(url=self.base_url+route)
                    parsed = await sent.read()
                    decoded = await parsed.decode()
                    return Payload(OPCODES.HTTP,json.loads(decoded),event_name="HTTP_REQUEST_RECIEVED")
                case "delete":
                    sent = await client.delete(self.base_url+route)
                    parsed = await sent.read()
                    decoded = parsed.decode()
                    return Payload(OPCODES.HTTP,d=json.loads(decoded),s="HTTP_REQUEST_RECIEVED")