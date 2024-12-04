from ..po_payload import _PermissionOverwritePayload
from ..overwrites import PermissionOverwrite

class PermissionOverwriteMapper:
    def __init__(self,dto: _PermissionOverwritePayload):
        self.data = dto
    
    
    def map(self):
        for key_outer,value in self.data.__to_be_conv.data.items():
            if key_outer not in PermissionOverwrite.__dict__.keys():
                self.data.__to_be_conv.data[key_outer] = value
                # adds fields that are specific to certain endpoints, if recieved with those fields
        return PermissionOverwrite(self.data.__to_be_conv.data)