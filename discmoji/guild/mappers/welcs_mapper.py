from ..welcs_payload import _WelcomeScreenPayload
from ..welcomescreen import WelcomeScreen



class WelcomeScreenMapper:
    def __init__(self, dto: _WelcomeScreenPayload):
        self.data = dto

    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in WelcomeScreen.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return WelcomeScreen(self.data.__to_be_conv.data)