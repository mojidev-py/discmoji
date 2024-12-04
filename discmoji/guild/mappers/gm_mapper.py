from ..gm_payload import _GuildMemberPayload
from ..guild_member import GuildMember

class GuildMemberMapper:
    def __init__(self, dto: _GuildMemberPayload):
        self.data = dto
    
    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in GuildMember.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return GuildMember(self.data.__to_be_conv.data)