from ..snowflake import Snowflake
from .resolved import ResolvedData
from .interuser import InteractionInput


class InteractionParams:
    """Contains extra info about the invoked application command."""
    def __init__(self,_dict: dict):
        self.id = Snowflake(_dict["id"])
        self.name = _dict["name"]
        self.resolved = ResolvedData(_dict["resolved"]) if _dict.get("resolved") else None
        self.parameters = [InteractionInput(userinput) for userinput in _dict["options"]] if _dict.get("options") else None
        self.guild_id = Snowflake(_dict["guild_id"]) if _dict.get("guild_id") else None
        self.user_id = Snowflake(_dict["target_id"]) if _dict.get("target_id") else None

