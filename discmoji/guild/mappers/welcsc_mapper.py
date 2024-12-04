from ..welcsc_payload import _WelcomeScreenChannelPayload
from ..welcomescreen import WelcomeScreenChannel

class WelcomeScreenChannelMapper:
    def __init__(self, dto: _WelcomeScreenChannelPayload):
        self.data = dto
    
    def map(self):
        return WelcomeScreenChannel(self.data.__to_be_conv.data)