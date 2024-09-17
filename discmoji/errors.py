class DiscmojiError(Exception):
    """ An error relating to the inner workings of Discmoji. """
    def __init__(self,msg: str):
        self.msg = msg
    def __str__(self):
        return f"Discmoji encountered an internal error: {self.msg}"

class DiscmojiAPIError(DiscmojiError):
    """ An error related to Discord API interactions in Discmoji. """
    def __str__(self):
        return f"An error occured when interacting with the Discord API: {self.msg}"
class DiscmojiCommandError(DiscmojiError):
    """ An error related to bot commands using Discmoji. """
    def __str__(self):
        return f"An error ocurred when executing/creating a bot command: {self.msg}"
   
   # For unknown/unspecified errors: `raise DiscmojiError("Error Message")`
   # For Discord API errors: `raise DiscmojiAPIError("Error Message")`
   # For command errors: `raise DiscmojiCommandError("Error Message")`
   # -- sample output --
   # DiscmojiError: Discmoji encountered an internal error while trying to initiate a connection or another error occured that raised this exception. error with message:
   # (Exception,(the default/builtin exception that it failed with's args)) blueblahhh
