from ..s_payload import _StickerPayload
from ..sticker import Sticker



class StickerMapper:
    def __init__(self, dto: _StickerPayload):
        self.data = dto

    
    def map(self):

        return Sticker(self.data.__to_be_conv.data)