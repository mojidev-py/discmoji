from typing import Optional,Dict,List
from .user import User
from .team import Team
from ._http import EndpointManager




class AppInfo:
    """A class that represents the application itself.
    Do not initialize this class. It will be initialized for you at bot connection."""
    def __init__(self,_data: Optional[Dict],endpoint_mgr: EndpointManager):
        self.id = int(_data.get("id"))
        self.name: str = _data.get("name")
        self.icon: str = _data.get("icon_hash")
        self.desc: str = _data.get("description")
        self.rpc_origins: Optional[List[str]] = _data.get("rpc_origins")
        self.public: bool = _data.get("bot_public")
        self.code_grant: bool = _data.get("bot_require_code_grant")
        self.tos_url: Optional[str] = _data.get("terms_of_service_url")
        self.privacy_policy_url: str = _data.get("privacy_policy_url")
        self.owner: User = User(_data.get("owner"))
        self.team: Team = Team(_data.get("team"),endpoint_mgr)
        self.guild_id = int(_data.get("guild_id"))
        self.cover_image: str = _data.get("cover_image")
        self.flags: int = _data.get("flags")
        self.approx_guild_count: int = _data.get("approximate_guild_count")
        self.approx_user_installs: int = _data.get("approximate_user_install_count")
        self.redirects: List[str] = _data.get("redirect_uris")