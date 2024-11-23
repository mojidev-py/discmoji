"""MIT License

Copyright (c) 2024 mojidev-py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from .types import IntentsBits

class BotIntents:
    def __init__(self):
        self.guilds = False
        """The following permissions are enabled with this intent: 
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
        """(Privileged Intent) The following permissions are enabled with this privileged intent:
  - `GUILD_MEMBER_ADD`
  - `GUILD_MEMBER_UPDATE`
  - `GUILD_MEMBER_REMOVE`
  - `THREAD_MEMBERS_UPDATE`"""
        self.guild_moderation = False
        """The following permissions are enabled with this intent:
  - `GUILD_AUDIT_LOG_ENTRY_CREATE`
  - `GUILD_BAN_ADD`
  - `GUILD_BAN_REMOVE`"""
        self.guild_expressions = False
        """The following permissions are enabled with this intent.
  - `GUILD_EMOJIS_UPDATE`
  - `GUILD_STICKERS_UPDATE`
  - `GUILD_SOUNDBOARD_SOUND_CREATE`
  - `GUILD_SOUNDBOARD_SOUND_UPDATE`
  - `GUILD_SOUNDBOARD_SOUND_DELETE`
  - `GUILD_SOUNDBOARD_SOUNDS_UPDATE`"""
        self.guild_integrations = False
        """The following permissions are enabled with this intent.
  - GUILD_INTEGRATIONS_UPDATE
  - INTEGRATION_CREATE
  - INTEGRATION_UPDATE
  - INTEGRATION_DELETE"""
        self.guild_webhooks = False
        """The following permission is enabled with this intent:
        - `WEBHOOKS_UPDATE`"""