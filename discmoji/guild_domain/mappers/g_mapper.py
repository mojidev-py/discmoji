from ..g_payload import _GuildPayload
from ..guild import Guild

class GuildMapper:
    def __init__(self, dto: _GuildPayload):
        self.data = dto
    
    
    def map(self):
        return Guild(self.data.__to_be_conv.data)