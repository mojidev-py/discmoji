from ._cli import __CLI__
from ...discmoji.types import initiatelogging, formatter

cli = __CLI__()
clihelpdict = {
    "shards": "Shows a list of shards that the bot is in, and info for that shard.",
    "push": "Pushes a change to a specific shard"
}



@cli._cli_cmd(name="help")
def clihelp(cmd: str):
    initiatelogging.info()