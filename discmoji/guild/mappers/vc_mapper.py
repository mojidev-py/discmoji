from ..vc_payload import _VoiceChannelPayload
from ..channel import VoiceChannel


class VoiceChannelMapper:
    def __init__(self,dto: _VoiceChannelPayload):
        self.data = dto
    
    def map(self):

        return VoiceChannel(self.data.__to_be_conv.data)