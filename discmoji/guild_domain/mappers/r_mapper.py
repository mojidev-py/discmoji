from ..r_payload import _RolePayload
from ..roles import Role


class RoleMapper:
    def __init__(self,dto: _RolePayload):
        self.data = dto
    
    def map(self):
        return Role(self.data.__to_be_conv.data)