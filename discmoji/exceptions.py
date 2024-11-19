"""Exceptions"""

class InternalDiscmojiException(Exception):
    """Something failed internally."""
    
    def __str__(self):
        return f"Failed due to internal error. Cause: {self.args}"