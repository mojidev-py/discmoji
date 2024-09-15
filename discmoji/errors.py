class DiscmojiError(Exception):
    """ An error relating to the inner workings of Discmoji. """
    def __init__(self,msg: str):
        self.msg = msg
    def __str__(self):
        return f"Discmoji encountered an internal error while trying to initiate a connection or another error occured that raised this exception. error with message:
    {self.args}: {self.msg}"
   
   # format to call: DiscmojiError('error text')
   # how this is called: DiscmojiError("blueblahhhh")
   # output: 
   # DiscmojiError: Discmoji encountered an internal error while trying to initiate a connection or another error occured that raised this exception. error with message:
   # (Exception,(the default/builtin exception that it failed with's args)) blueblahhh