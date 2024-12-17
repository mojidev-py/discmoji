from ..e_payload import _EmojiPayload
from ..emoji import Emoji

class EmojiMapper:
    def __init__(self,dto: _EmojiPayload):
        self.data = dto

    
    def map(self):
        return Emoji(self.data.__to_be_conv.data)