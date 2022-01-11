from contextlib import suppress

from unidecode import unidecode
import nextcord
from nextcord.ext import commands

END_OF_SENTENCE_CHARS = [".", "!", "?", ",", ";", ":"]


class Dad(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message: nextcord.Message) -> None:
        if message.author.bot or message.author.id == self.bot.user.id:
            return
        content = unidecode(message.content.lower())
        location = None
        with suppress(ValueError):
            location = message.content.lower().split(" ").index("im")
        with suppress(ValueError):
            location = message.content.lower().split(" ").index("i'm")
        if location is None:
            return
        name = ""
        for i in message.content.split(" ")[
            location + 1 : min(location + 11, len(message.content.split(" ")))
        ]:
            if i[-1] in END_OF_SENTENCE_CHARS:
                name += i[:-1] + " "
                break
            else:
                name += i + " "
        if name == "":
            return
        await message.channel.send("Hi {}, I'm dad!".format(name[:-1]))

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Dad(bot))