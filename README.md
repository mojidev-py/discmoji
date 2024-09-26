# discmoji


[![CodeFactor](https://www.codefactor.io/repository/github/mojidev-py/discmoji/badge)](https://www.codefactor.io/repository/github/mojidev-py/discmoji)  ![License](https://img.shields.io/badge/License-MIT-blue?labelColor=gray&style=flat)

[discmoji on PyPI](https://pypi.org/project/discmoji/)

## ❔ What is Discmoji?
Discmoji is an API wrapper for Discord, made for fun!
This isn't meant for production use, and if it does get used a lot, the library will get a redesign.

## 💡 Suggestions? 
Open a issue with the label `enhancement`, and follow the template!

## ⭐️ Contributing
Discmoji needs contributors! contact me (mojidev-py) at `pycharmdudeig@gmail.com` to become one!

## 📖 Example
```python
from discmoji import *
import asyncio

Client = Bot(token="discord bot token",intents=123213123) 

@Client.command(name="example command")
async def commd(ctx: Invoked):
    asyncio.run(Client.get_guild(1234567))

@commd.error()
async def example_error(ctx: Invoked,error: Exception):
    print("Something bad happened!")

asyncio.run(Client.connect)
```

### 🗓️ Release Date???
> Around October 17th or September 30th (0.3.0 is going to be a full release)
## 📣 ANNOUNCEMENTS/FAQ
>### 🚀 Development Schedule???
>The development schedule will have fluctuations, but expect atleast 5 commits a week.
>###  🤞  1.0.0?
> 1.0.0 is estimated to be made around March 2025, all the way to late May 2025 all the way to July 2025 (not very optimistic date, ik)
>### ❔ Will this _ever_ be finished?
> Fingers Crossed!
