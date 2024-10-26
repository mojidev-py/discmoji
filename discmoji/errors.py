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
class DiscmojiRatelimit(Warning):
    def __init__(self,msg: str):
        def __str__(self):
            return f"Discmoji is currently being ratelimited. Rerun the bot in: {self.msg}s."

class DiscmojiConnectionError(DiscmojiError):
    """ An error related to connection issues in Discmoji. """
    def __str__(self):
        return f"An error occurred with the connection: {self.msg}"

class DiscmojiTimeoutError(DiscmojiError):
    """ An error related to timeout issues in Discmoji. """
    def __str__(self):
        return f"An error occurred due to a timeout: {self.msg}"

class DiscmojiPermissionError(DiscmojiError):
    """ An error related to permission issues in Discmoji. """
    def __str__(self):
        return f"An error occurred due to insufficient permissions: {self.msg}"

class DiscmojiValidationError(DiscmojiError):
    """ An error related to validation issues in Discmoji. """
    def __str__(self):
        return f"An error occurred due to validation failure: {self.msg}"

class DiscmojiNotFoundError(DiscmojiError):
    """ An error related to not found issues in Discmoji. """
    def __str__(self):
        return f"An error occurred because the requested resource was not found: {self.msg}"

class DiscmojiRateLimitError(DiscmojiError):
    """ An error related to rate limiting issues in Discmoji. """
    def __str__(self):
        return f"An error occurred due to rate limiting: {self.msg}"

class DiscmojiAuthenticationError(DiscmojiError):
    """ An error related to authentication issues in Discmoji. """
    def __str__(self):
        return f"An error occurred due to authentication failure: {self.msg}"

class DiscmojiParsingError(DiscmojiError):
    """ An error related to parsing issues in Discmoji. """
    def __str__(self):
        return f"An error occurred while parsing data: {self.msg}"

class DiscmojiUnknownError(DiscmojiError):
    """ An unknown error in Discmoji. """
    def __str__(self):
        return f"An unknown error occurred: {self.msg}"

class DiscmojiDeprecationWarning(Warning):
    """ A warning related to deprecated features in Discmoji. """
    def __init__(self, msg: str):
        self.msg = msg
    def __str__(self):
        return f"Discmoji is using a deprecated feature: {self.msg}"

class DiscmojiConfigurationWarning(Warning):
    """ A warning related to configuration issues in Discmoji. """
    def __init__(self, msg: str):
        self.msg = msg
    def __str__(self):
        return f"Discmoji configuration issue: {self.msg}"

class DiscmojiPerformanceWarning(Warning):
    """ A warning related to performance issues in Discmoji. """
    def __init__(self, msg: str):
        self.msg = msg
    def __str__(self):
        return f"Discmoji performance issue: {self.msg}"

class DiscmojiSecurityWarning(Warning):
    """ A warning related to security issues in Discmoji. """
    def __init__(self, msg: str):
        self.msg = msg
    def __str__(self):
        return f"Discmoji security issue: {self.msg}"
