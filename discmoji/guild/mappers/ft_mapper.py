from ..ft_payload import _ForumTagsPayload
from ...types import ForumTag

class ForumTagMapper:
    def __init__(self, dto: _ForumTagsPayload):
        self.data = dto
    
    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in ForumTag.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return ForumTag(self.data.__to_be_conv.data)


