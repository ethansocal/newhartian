import os

import discord
import nextcord
from nextcord.ext import commands


class Bot(commands.Bot):
    async def on_ready(self) -> None:
        print("Logged in as {}#{}".format(self.user.name, self.user.discriminator))
        self.load_all_extensions()

    def load_all_extensions(self) -> None:
        for file in os.listdir("bot/ext"):
            if file.endswith(".py") and not file.startswith("_"):
                self.load_extension("bot.ext." + file[:-3])
                print("Loaded extension {}".format(file[:-3]))
