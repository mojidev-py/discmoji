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