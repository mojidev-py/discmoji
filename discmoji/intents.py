from typing import *
from enum import Enum

class IntentsBits(Enum):
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
    GUILD_BANS = 1 << 26
    GUILD_INVITES = 1 << 27


class BotIntents:
    """A abstraction layer over a bitfield containing the intents your bot needs. We also offer pre-made configurations.
    - `set_manual` param
      - an internal param used by the class methods to set the result_field
    - `result_field` attribute
      -  Used to send the bitfield converted to an int to the gateway."""
    def __init__(self, _set_manual: Optional[int | Any]):
        self.result_field: int = _set_manual
        self.guilds = IntentsBits.GUILDS
        
    @classmethod
    def all(cls):
        """A method that creates an BotIntents object with every intent."""
        result_field = (
            IntentsBits.GUILDS
            | IntentsBits.GUILD_MEMBERS
            | IntentsBits.GUILD_MODERATION
            | IntentsBits.GUILD_EMOJIS_STICKERS
            | IntentsBits.GUILD_INTEGRATIONS
            | IntentsBits.GUILD_WEBHOOKS
            | IntentsBits.GUILD_INVITES
            | IntentsBits.GUILD_VOICE_STATES
            | IntentsBits.GUILD_PRESENCES
            | IntentsBits.GUILD_MESSAGES
            | IntentsBits.GUILD_MESSAGE_REACTIONS
            | IntentsBits.GUILD_MESSAGE_TYPING
            | IntentsBits.DIRECT_MESSAGES
            | IntentsBits.DIRECT_MESSAGE_REACTIONS
            | IntentsBits.DIRECT_MESSAGE_TYPING
            | IntentsBits.MESSAGE_CONTENT
            | IntentsBits.GUILD_SCHEDULED_EVENTS
            | IntentsBits.AUTO_MODERATION_CONFIGURATION
            | IntentsBits.AUTO_MODERATION_EXECUTION
            | IntentsBits.GUILD_MESSAGE_POLLS
            | IntentsBits.DIRECT_MESSAGE_POLLS
            | IntentsBits.GUILD_BANS
            | IntentsBits.GUILD_INVITES
        )
        return cls(_set_manual=result_field)

    @classmethod
    def default(cls):
        """A method that creates a BotIntents object with the default intents."""
        result_field = (
            IntentsBits.GUILDS
            | IntentsBits.GUILD_MEMBERS
            | IntentsBits.GUILD_MESSAGES
            | IntentsBits.GUILD_MESSAGE_REACTIONS
            | IntentsBits.DIRECT_MESSAGES
            | IntentsBits.DIRECT_MESSAGE_REACTIONS
        )
        return cls(_set_manual=result_field)

    @classmethod
    def minimal(cls):
        """A method that creates a BotIntents object with the minimal required intents."""
        result_field = (
            IntentsBits.GUILDS
            | IntentsBits.GUILD_MESSAGES
        )
        return cls(_set_manual=result_field)

    @classmethod
    def custom(cls, *intents: IntentsBits):
        """A method that creates a BotIntents object with custom intents."""
        result_field = 0
        for intent in intents:
            result_field |= intent
        return cls(_set_manual=result_field)
