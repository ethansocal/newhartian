from .bot import Bot
import os


print("running")
bot = Bot("!")
bot.run(os.environ["TOKEN"])