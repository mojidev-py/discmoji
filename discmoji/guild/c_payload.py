from ..types import RequestBody,WebsocketPayload



class _ChannelPayload:
    def __init__(self,json_data: WebsocketPayload | RequestBody):
        self.__to_be_conv = json_data