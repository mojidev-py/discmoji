from ..types import RequestBody,WebsocketPayload


class _RolePayload:
    def __init__(self,json_data: WebsocketPayload | RequestBody):
        self.__to_be_conv = json_data