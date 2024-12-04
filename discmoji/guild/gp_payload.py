from ..types import RequestBody,WebsocketPayload


class _GuildPreviewPayload:
    def __init__(self, data: RequestBody | WebsocketPayload):
        self.__to_be_conv = data