from ..welcsc_payload import _WelcomeScreenChannelPayload
from ..welcomescreen import WelcomeScreenChannel

class WelcomeScreenChannelMapper:
    def __init__(self, dto: _WelcomeScreenChannelPayload):
        self.data = dto
    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in WelcomeScreenChannel.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return WelcomeScreenChannel(self.data.__to_be_conv.data)