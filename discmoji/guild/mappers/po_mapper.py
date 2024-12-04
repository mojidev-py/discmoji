from ..po_payload import _PermissionOverwritePayload
from ..overwrites import PermissionOverwrite

class PermissionOverwriteMapper:
    def __init__(self,dto: _PermissionOverwritePayload):
        self.data = dto
    
    
    def map(self):
        return PermissionOverwrite(self.data.__to_be_conv.data)