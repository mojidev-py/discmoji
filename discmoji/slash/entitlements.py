from ..snowflake import Snowflake
import datetime




class Entitlement:
    def __init__(self,_dict: dict):
        self.id = Snowflake(_dict["id"])
        self.sku_id = Snowflake(_dict["sku_id"])
        self.user_id = Snowflake(_dict["user_id"]) if _dict.get("user_id") else None
        self._type: int = _dict["type"]
        self.deleted: bool = _dict["deleted"]
        self.starts_at = datetime.datetime.fromisoformat(_dict["starts_at"])
        self.ends_at = datetime.datetime.fromisoformat(_dict["ends_at"])
        self.guild_id = Snowflake(_dict["guild_id"]) if _dict.get("guild_id") else None
        self.consumed = _dict.get("consumed")

