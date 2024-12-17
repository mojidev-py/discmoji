from ..welcs_payload import _WelcomeScreenPayload
from ..welcomescreen import WelcomeScreen



class WelcomeScreenMapper:
    def __init__(self, dto: _WelcomeScreenPayload):
        self.data = dto

    
    def map(self):
        return WelcomeScreen(self.data.__to_be_conv.data)