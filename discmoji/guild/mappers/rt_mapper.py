from ..rt_payload import _RoleTagsPayload
from ...types import RoleTags


class RoleTagMapper:
    def __init__(self, dto: _RoleTagsPayload):
        self.data = dto

    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in RoleTags.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return RoleTags(self.data.__to_be_conv.data)