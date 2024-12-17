"""MIT License

Copyright (c) 2024 mojidev-py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this event notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from ._types import IntentsBits
from typing import Self
from .exceptions import InternalDiscmojiException
class BotIntents:
  """Represents your bot's gateway intents. 
  You can turn intents on and off using the corresponding attribute, and flipping its value to True or False. 
  Everything is set false by default."""
  def __init__(self):
        self.guilds = False
        """The following events are enabled with this intent: 
  - `GUILD_CREATE`
  - `GUILD_UPDATE`
  - `GUILD_DELETE`
  - `GUILD_ROLE_CREATE`
  - `GUILD_ROLE_UPDATE`
  - `GUILD_ROLE_DELETE`
  - `CHANNEL_CREATE`
  - `CHANNEL_UPDATE`
  - `CHANNEL_DELETE`
  - `CHANNEL_PINS_UPDATE`
  - `THREAD_CREATE`
  - `THREAD_UPDATE`
  - `THREAD_DELETE`
  - `THREAD_LIST_SYNC`
  - `THREAD_MEMBER_UPDATE`
  - `THREAD_MEMBERS_UPDATE`
  - `STAGE_INSTANCE_CREATE`
  - `STAGE_INSTANCE_UPDATE`
  - `STAGE_INSTANCE_DELETE`"""
        self.guild_members = False
        """(Privileged Intent) The following events are enabled with this privileged intent:
  - `GUILD_MEMBER_ADD`
  - `GUILD_MEMBER_UPDATE`
  - `GUILD_MEMBER_REMOVE`
  - `THREAD_MEMBERS_UPDATE`"""
        self.guild_moderation = False
        """The following events are enabled with this intent:
  - `GUILD_AUDIT_LOG_ENTRY_CREATE`
  - `GUILD_BAN_ADD`
  - `GUILD_BAN_REMOVE`"""
        self.guild_expressions = False
        """The following events are enabled with this intent.
  - `GUILD_EMOJIS_UPDATE`
  - `GUILD_STICKERS_UPDATE`
  - `GUILD_SOUNDBOARD_SOUND_CREATE`
  - `GUILD_SOUNDBOARD_SOUND_UPDATE`
  - `GUILD_SOUNDBOARD_SOUND_DELETE`
  - `GUILD_SOUNDBOARD_SOUNDS_UPDATE`"""
        self.guild_integrations = False
        """The following events are enabled with this intent.
  - `GUILD_INTEGRATIONS_UPDATE`
  - `INTEGRATION_CREATE`
  - `INTEGRATION_UPDATE`
  - `INTEGRATION_DELETE`"""
        self.guild_webhooks = False
        """The following event is enabled with this intent:
        - `WEBHOOKS_UPDATE`"""
        self.guild_invites = False
        """ The following events are enabled with this intent: 
  - `INVITE_CREATE`
  - `INVITE_DELETE`"""
        self.guild_voice_states = False
        """The following events are enabled with this intent:
  - `VOICE_CHANNEL_EFFECT_SEND`
  - `VOICE_STATE_UPDATE`"""
        self.guild_presences = False
        """(Privileged) The following events are enabled with this privileged intent:
        - `PRESENCE_UPDATE`"""
        self.guild_messages = False
        """The following events are enabled with this intent:
  - `MESSAGE_CREATE`
  - `MESSAGE_UPDATE`
  - `MESSAGE_DELETE`
  - `MESSAGE_DELETE_BULK`"""
        self.guild_message_reactions = False
        """The following events are enabled with this intent:  
  - `MESSAGE_REACTION_ADD`
  - `MESSAGE_REACTION_REMOVE`
  - `MESSAGE_REACTION_REMOVE_ALL`
  - `MESSAGE_REACTION_REMOVE_EMOJI` """
        self.guild_message_typing = False
        """The following event is enabled with this intent:
        - `TYPING_START`"""
        self.dm = False
        """The following events are enabled with this intent:
  - `MESSAGE_CREATE`
  - `MESSAGE_UPDATE`
  - `MESSAGE_DELETE`
  - `CHANNEL_PINS_UPDATE`"""
        self.dm_reactions = False
        """The following events are enabled with this intent:
  - `MESSAGE_REACTION_ADD`
  - `MESSAGE_REACTION_REMOVE`
  - `MESSAGE_REACTION_REMOVE_ALL`
  - `MESSAGE_REACTION_REMOVE_EMOJI`"""
        self.dm_typing = False
        """The following events are enabled with this intent:
          - `TYPING_START`"""
        self.message_content = False
        """(Privileged) No events are enabled with this intent, but instead, makes you eligible to recieve message content. Necessary for prefix commands to work."""
        self.guild_scheduled_events = False
        """The following events are enabled with this intent:
  - `GUILD_SCHEDULED_EVENT_CREATE`
  - `GUILD_SCHEDULED_EVENT_UPDATE`
  - `GUILD_SCHEDULED_EVENT_DELETE`
  - `GUILD_SCHEDULED_EVENT_USER_ADD`
  - `GUILD_SCHEDULED_EVENT_USER_REMOVE`"""
        self.automod_config = False
        """The following events are enabled with this intent:
  - `AUTO_MODERATION_RULE_CREATE`
  - `AUTO_MODERATION_RULE_UPDATE`
  - `AUTO_MODERATION_RULE_DELETE` """
        self.automod_execution = False
        """The following event is enabled with this intent:
          - `AUTO_MODERATION_ACTION_EXECUTION`"""
        self.guild_message_polls = False
        """The following events are enabled with this intent:
  - `MESSAGE_POLL_VOTE_ADD`
  - `MESSAGE_POLL_VOTE_REMOVE`"""
        self.dm_polls = False
        """The following events are enabled with this intent:
  - `MESSAGE_POLL_VOTE_ADD`
  - `MESSAGE_POLL_VOTE_REMOVE`"""
  
      
  @classmethod
  def _conv_intents(cls,input: int) -> Self:
        # literally just a copy and paste from Permissions functions
        """Converts from a raw integer representation of intents to self."""
        return_class = cls()
        bytes_input = bytes(input)
        for key,item in IntentsBits.__members__.items():
                if bytes_input & bytes(item):
                    try:    
                        setattr(return_class,key,True)
                    except AttributeError as e:
                        raise InternalDiscmojiException(e.args)
        return return_class
  
  def _deconv_intents(self):
        """An internal utility function that turns the Intents object back into an integer. """
        integer = 0
        for item,value in self.__dict__.items():
            if callable(value):
                continue
            else:
                if value:
                    integer += IntentsBits.__members__[item.upper()]
        return integer