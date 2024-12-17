from ..gm_payload import _GuildMemberPayload
from ..guild_member import GuildMember

class GuildMemberMapper:
    def __init__(self, dto: _GuildMemberPayload):
        self.data = dto
    
    
    def map(self):
        return GuildMember(self.data.__to_be_conv.data)