from ..g_payload import _GuildPayload
from ..guild import Guild

class GuildMapper:
    def __init__(self, dto: _GuildPayload):
        self.data = dto
    
    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in Guild.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return Guild(self.data.__to_be_conv.data)