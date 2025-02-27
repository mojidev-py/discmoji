from ..snowflake import Snowflake

class ResolvedData:
    """Hosts snowflakes that map to channels, guilds, members etc."""
    def __init__(self,_dict: dict):
        self.users = [Snowflake(user) for user in _dict["users"]] if _dict.get("users") else None
        self.members = [Snowflake(user) for user in _dict["members"]] if _dict.get("members") else None
        self.roles = [Snowflake(role) for role in _dict["roles"]] if _dict.get("roles") else None
        self.channels = [Snowflake(channel) for channel in _dict["channels"]] if _dict.get("channels") else None
        self.messages = [Snowflake(message) for message in _dict["messages"]] if _dict.get("messages") else None
        self.attachments = [Snowflake(attachment) for attachment in _dict["attachments"]] if _dict.get("attachments") else None