from .._types import WebsocketPayload,RequestBody

class _PermissionOverwritePayload:
    def __init__(self,json_data: WebsocketPayload | RequestBody):
        self.__to_be_conv = json_data