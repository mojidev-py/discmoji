from ..ft_payload import _ForumTagsPayload
from ...types import ForumTag

class ForumTagMapper:
    def __init__(self, dto: _ForumTagsPayload):
        self.data = dto
    
    
    def map(self):
        return ForumTag(self.data.__to_be_conv.data)


