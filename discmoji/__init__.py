"""# DISCMOJI 0.0.1
A discord api wrapper, made for fun.
Pre-alpha, so bugs may be present."""

from guild import *
from ._gateway import DiscordWebsocket
from ._http import HttpManager
from .intents import BotIntents
from .user import User
from .types import *
from .exceptions import *
from .decoration import AvatarDecoration
from .snowflake import Snowflake
