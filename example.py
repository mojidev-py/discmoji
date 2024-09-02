import discmoji
from discmoji import *

Client = Bot(token="blah blah",intents=123213123) 

# this is subject to change


@Client.command(name="cool")
# debug: command not commanding into command ;(
async def cool(ctx: Invoked):
    await Client.get_guild(id=1234567)


