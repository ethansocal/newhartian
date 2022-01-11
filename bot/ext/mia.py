import random

import nextcord
from nextcord.ext import commands

from .. import constants


class MiaCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.Cog.listener("on_member_join")
    async def on_member_join(self, member: nextcord.Member) -> None:
        if member.id == constants.MIA:
            await self.bot.get_channel(constants.GENERAL).send(
                f":warning::warning::warning: {member.mention()} HAS JOINED!!!!!!! RUN FOR YOUR LIVES!!!!!!!! :warning::warning::warning:"
            )
            return
        elif "mia" in member.name.lower():
            await self.bot.get_channel(constants.GENERAL).send(
                f":warning::warning: {member.mention()} has a {random.randint(50, 90)}% chance of being Mia! :warning::warning:"
            )
            return
        await self.bot.get_channel(constants.GENERAL).send(
            f":warning: {member.mention()} has a {random.randint(10, 50)}% chance of being Mia. :warning:"
        )


def setup(bot: commands.Bot) -> None:
    bot.add_cog(MiaCog(bot))
