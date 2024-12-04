from ..fc_payload import _ForumChannelPayload
from ..channel import ForumChannel


class ForumChannelMapper:
    def __init__(self, dto: _ForumChannelPayload):
        self.data = dto
    
    
    def map(self):
        return ForumChannel(self.data.__to_be_conv.data)        