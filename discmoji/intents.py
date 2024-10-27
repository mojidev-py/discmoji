from typing import *
from enum import Enum

class Bitfield(Enum):
    GUILDS = 1 << 0
    GUILD_MEMBERS = 1 << 1
    GUILD_MODERATION = 1 << 2
    GUILD_EMOJIS_STICKERS = 1 << 3
    GUILD_INTEGRATIONS = 1 << 4
    GUILD_WEBHOOKS = 1 << 5
    GUILD_INVITES = 1 << 6
    GUILD_VOICE_STATES = 1 << 7
    GUILD_PRESENCES = 1 << 8
    GUILD_MESSAGES = 1 << 9
    GUILD_MESSAGE_REACTIONS = 1 << 10
    GUILD_MESSAGE_TYPING = 1 << 11
    DIRECT_MESSAGES = 1 << 12
    DIRECT_MESSAGE_REACTIONS = 1 << 13
    DIRECT_MESSAGE_TYPING = 1 << 14
    MESSAGE_CONTENT = 1 << 15
    GUILD_SCHEDULED_EVENTS = 1 << 16
    AUTO_MODERATION_CONFIGURATION = 1 << 20
    AUTO_MODERATION_EXECUTION = 1 << 21
    GUILD_MESSAGE_POLLS = 1 << 24
    DIRECT_MESSAGE_POLLS = 1 << 25


class BotIntents:
    """A abstraction layer over a Bitfield containing the intents your bot needs. We also offer pre-made configurations.
    - `set_manual` param
      - an internal param used by the class methods to set the result_field
    - `result_field` attribute
      -  Used to send the Bitfield converted to an int to the gateway."""
    def __init__(self, _set_manual: Optional[int | Any]):
        self.result_field: int = _set_manual
        
    @classmethod
    def all(cls):
        """A method that creates an BotIntents object with every intent."""
        result_field = (
           Bitfield.GUILDS.value
            | Bitfield.GUILD_MEMBERS.value
            | Bitfield.GUILD_MODERATION.value
            | Bitfield.GUILD_EMOJIS_STICKERS.value
            | Bitfield.GUILD_INTEGRATIONS.value
            | Bitfield.GUILD_WEBHOOKS.value
            | Bitfield.GUILD_INVITES.value
            | Bitfield.GUILD_VOICE_STATES.value
            | Bitfield.GUILD_PRESENCES.value
            | Bitfield.GUILD_MESSAGES.value
            | Bitfield.GUILD_MESSAGE_REACTIONS.value
            | Bitfield.GUILD_MESSAGE_TYPING.value
            | Bitfield.DIRECT_MESSAGES.value
            | Bitfield.DIRECT_MESSAGE_REACTIONS.value
            | Bitfield.DIRECT_MESSAGE_TYPING.value
            | Bitfield.MESSAGE_CONTENT.value
            | Bitfield.GUILD_SCHEDULED_EVENTS.value
            | Bitfield.AUTO_MODERATION_CONFIGURATION.value
            | Bitfield.AUTO_MODERATION_EXECUTION.value
            | Bitfield.GUILD_MESSAGE_POLLS.value
            | Bitfield.DIRECT_MESSAGE_POLLS.value
        )
        return cls(_set_manual=result_field)

    
    
