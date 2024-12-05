"""Exceptions"""

class InternalDiscmojiException(Exception):
    """Something failed internally."""
    
    def __str__(self):
        return f"[DiscmojiError] Failed due to internal error. Cause: {self.args}"


class DiscmojiRetrievalError(Exception):
    """Something failed when trying to retrieve another thing."""
    def __init__(self,method: str,string: str):
        self.method = method
        self.message = string
    
    def __str__(self):
        return f"[DiscmojiError] Failed while running {self.method}: {self.message}"


class Forbidden(Exception):
    """The bot does not have the permissions to perform this action."""
    
    def __str__(self):
        return f"[403] Bot is forbidden to access resource. Check permissions for details."

class UnknownHTTPError(Exception):
    """An unknown http error has occured"""
    def __str__(self):
        return f"[Error Code: {self.args[0]}]: {self.args[1]}"