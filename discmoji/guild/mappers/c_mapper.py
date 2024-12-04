from ..c_payload import _ChannelPayload
from ..channel import Channel

class ChannelMapper:
    def __init__(self, data: _ChannelPayload):
        self.data = data
        
    
    def map(self):
        return Channel(self.data.__to_be_conv.data)
