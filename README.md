# discmoji


[![CodeFactor](https://www.codefactor.io/repository/github/mojidev-py/discmoji/badge)](https://www.codefactor.io/repository/github/mojidev-py/discmoji)  ![License](https://img.shields.io/badge/License-MIT-blue?labelColor=gray&style=flat) [![PyPI - Version](https://img.shields.io/pypi/v/discmoji)](https://pypi.org/project/discmoji/)
 ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/mojidev-py/discmoji) [![PyPI Downloads](https://static.pepy.tech/badge/discmoji)](https://pepy.tech/projects/discmoji)


> ### NOTE:
> Discmoji is ok for basic bot making at the moment. We are planning on adding support for slash commands and such in v0.1.4.

## ❔ What is Discmoji?
Discmoji is an API wrapper for Discord, made for fun!
This isn't meant for production use, and if it does get used a lot, the library will get a redesign.

## 💡 Suggestions? 
Open a issue with the label `enhancement`, and follow the template!

## ⭐️ Contributing
Discmoji needs contributors! contact me (mojidev-py) at `pycharmdudeig@gmail.com` to become one!

## 📖 Example
Replace `DISCORD_BOT_TOKEN` with your actual bot token.
```python
from discmoji import *

DISCORD_BOT_TOKEN = "1234567890"

Client = Bot(token=DISCORD_BOT_TOKEN,intents=123213123,prefix="?") 

@Client.prefix_command(name="example_command")
async def commd(ctx: PrefixContext):
    ctx.send("Test from your most amazing bot!")

@commd.error()
async def example_error(ctx: Invoked,error: Exception):
    print("Something bad happened!")

Client.connect()
```
## 📣 ANNOUNCEMENTS/FAQ


>### BACK FROM HIATUS
> BACK FROM HIATUS (just got really demotivated in programming, sorry for the delay)
>###  🤞  1.0.0?
> 1.0.0 is going to come out in 2025. No solid dates yet!
>### ❔ Will this _ever_ be finished?
> Fingers Crossed!

### Example
![Example of how console looks like with discmoji running]({141AA152-BF23-45FA-908B-DFBEB548EB0D}.png)
