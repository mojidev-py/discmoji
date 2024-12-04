from ..fc_payload import _ForumChannelPayload
from ..channel import ForumChannel


class ForumChannelMapper:
    def __init__(self, dto: _ForumChannelPayload):
        self.data = dto
    
    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in ForumChannel.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return ForumChannel(self.data.__to_be_conv.data)        