from .._types import RequestBody,WebsocketPayload

class _RoleTagsPayload:
    def __init__(self,json_data: WebsocketPayload | RequestBody):
        self.__to_be_conv = json_data