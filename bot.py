import SlashDiscord
from dotenv import dotenv_values
import sys


def ping(ctx):
    return f"Hey {ctx.member.user.username}"

if(__name__ == "__main__"):
    config = dotenv_values(".env")
    _ping = SlashDiscord.Command("ping", 1, "ping", handler=ping)
    _client = SlashDiscord.Client(config["TOKEN"], 0, config["APP_ID"], log_level=10, commands=[_ping])
    if("-d" in sys.argv):
        _client.deregister()
        _client.register()
    elif("-r" in sys.argv):
        _client.register()
    _client.connect()
