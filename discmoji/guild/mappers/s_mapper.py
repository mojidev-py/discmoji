from ..s_payload import _StickerPayload
from ..sticker import Sticker



class StickerMapper:
    def __init__(self, dto: _StickerPayload):
        self.data = dto

    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in Sticker.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return Sticker(self.data.__to_be_conv.data)