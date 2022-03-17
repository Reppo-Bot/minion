import SlashDiscord
from dotenv import dotenv_values
import sys
import requests as r

def leaderboard(ctx):
    res = r.post("http://bot.localhost:8080/command/callCommand", json=ctx)
    if(res.json()["message"] != ""):
        return {'error' : True, "message" : res.json()['message']}
    return {'error' : False}

if(__name__ == "__main__"):
    config = dotenv_values(".env")
    _command = SlashDiscord.Command("leaderboard", 1, "just testing", handler=leaderboard, respond=False)
    _client = SlashDiscord.Client(config["TOKEN"], 0, config["APP_ID"], log_level=10, commands=[_command])
    if("-d" in sys.argv):
        _client.deregister()
        _client.register()
    elif("-r" in sys.argv):
        _client.register()
    _client.connect()
