import os

from .bot import Bot

print("running")
bot = Bot("!")
bot.run(os.environ["TOKEN"])
