from ..e_payload import _EmojiPayload
from ..emoji import Emoji

class EmojiMapper:
    def __init__(self,dto: _EmojiPayload):
        self.data = dto

    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in Emoji.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return Emoji(self.data.__to_be_conv.data)