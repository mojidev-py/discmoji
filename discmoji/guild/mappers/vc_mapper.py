from ..vc_payload import _VoiceChannelPayload
from ..channel import VoiceChannel


class VoiceChannelMapper:
    def __init__(self,dto: _VoiceChannelPayload):
        self.data = dto
    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in VoiceChannel.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return VoiceChannel(self.data.__to_be_conv.data)