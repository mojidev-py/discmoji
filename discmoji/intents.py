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


class BotIntents:
    """A abstraction layer over a bitfield containing the intents your bot needs. We also offer pre-made configurations."""
    def __init__(self):
        self.result_field: int = 0
        
    
    
    @classmethod
    def default(self):
        """A method that creates an BotIntents object with every intent, except:
        - Privileged Intents
        - Automod Intents
        - Direct Messages """
        self.result_field = IntentsBits.GUILDS | IntentsBits.GUILD_MODERATION | IntentsBits.GUILD_EMOJIS_STICKERS | IntentsBits.GUILD_INTEGRATIONS | IntentsBits.GUILD_WEBHOOKS | IntentsBits.GUILD_INVITES | IntentsBits.GUILD_VOICE_STATES | IntentsBits.GUILD_MESSAGES | IntentsBits.GUILD_MESSAGE_REACTIONS | IntentsBits.GUILD_MESSAGE_TYPING | IntentsBits.GUILD_SCHEDULED_EVENTS | IntentsBits.GUILD_MESSAGE_POLLS
    
    
    