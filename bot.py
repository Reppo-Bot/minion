import SlashDiscord
from dotenv import dotenv_values
import sys
import requests as r

def default(ctx):
    res = r.post("http://bot.localhost:8080/callCommand", json=ctx)
    _res = res.json()
    if("failed" in _res):
        print(f"Failed command, responding with {_res['failed']}")
        return _res["failed"]

def ping(ctx):
    return f"Hello {ctx.member.nick}!"

def vibeCheck(ctx):
    res = r.post("http://bot.localhost:8080/callVibecheck", json=ctx)
    _res = res.json()
    if("failed" in _res):
        print(f"Failed command, responding with {_res['failed']}")
        return _res["failed"]

def leaderboard(ctx):
    res = r.post("http://bot.localhost:8080/callLeaderboard", json=ctx)
    _res = res.json()
    if("failed" in _res):
        print(f"Failed command, responding with {_res['failed']}")
        return _res["failed"]

if(__name__ == "__main__"):
    vibeCheckOptions = [{
        "name": "person",
        "type": 6,
        "description": "Person to check",
        "required": False
    }]

    config = dotenv_values(".env")
    _default = SlashDiscord.Command("default", 1, "default command", handler=default, respond=False)
    _ping = SlashDiscord.Command("ping", 1, "say hello", handler=ping, respond=True)
    _vibeCheck = SlashDiscord.Command("vibecheck", 1, "Check a users rep", handler=vibeCheck, respond=False, options=vibeCheckOptions)
    _leaderboard = SlashDiscord.Command("leaderboard", 1, "Check leaderboards", handler=leaderboard, respond=False)
    _client = SlashDiscord.Client(config["TOKEN"], 0, config["APP_ID"], log_level=10, commands=[_ping,_vibeCheck,_leaderboard])
    _client.setDefault(_default)
    if("-d" in sys.argv):
        _client.deregister()
        _client.register()
    elif("-r" in sys.argv):
        _client.register()
    _client.connect()
