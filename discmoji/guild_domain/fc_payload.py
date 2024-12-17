from .._types import WebsocketPayload, RequestBody

class _ForumChannelPayload:
    def __init__(self,json_data: WebsocketPayload | RequestBody):
        self.__to_be_conv = json_data