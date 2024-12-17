from ..rt_payload import _RoleTagsPayload
from ... import RoleTags


class RoleTagMapper:
    def __init__(self, dto: _RoleTagsPayload):
        self.data = dto

    
    def map(self):
        return RoleTags(self.data.__to_be_conv.data)