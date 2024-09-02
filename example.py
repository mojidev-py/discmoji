import discmoji
from discmoji import *
import asyncio

Client = Bot(token="blah blah",intents=123213123) 

# this is subject to change


@Client.command(name="test1 one")
def commd(ctx: Invoked):
    asyncio.run(Client.get_guild(1234567))

@commd.error
def error_cool(ctx: Invoked,error: Exception):
    print("ooh thank you demo-py!!")

asyncio.run(Client.connect)