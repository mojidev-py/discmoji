from ..c_payload import _ChannelPayload
from ..channel import Channel

class ChannelMapper:
    def __init__(self, data: _ChannelPayload):
        self.data = data
        
    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in Channel.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return Channel(self.data.__to_be_conv.data)
