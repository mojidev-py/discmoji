from ..gp_payload import _GuildPreviewPayload
from ..preview import GuildPreview    
    
class GuildPreviewMapper:    
    def __init__(self, dto: _GuildPreviewPayload):
        self.data = dto
    
    
    def map(self):
        return GuildPreview(self.data.__to_be_conv.data)