from ..r_payload import _RolePayload
from ..roles import Role


class RoleMapper:
    def __init__(self,dto: _RolePayload):
        self.data = dto
    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in Role.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return Role(self.data.__to_be_conv.data)