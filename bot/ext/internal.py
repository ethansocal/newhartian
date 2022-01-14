from aioconsole import aexec
from nextcord.ext import commands


class InternalCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    async def eval(self, ctx: commands.Context, *, code: str) -> None:
        if ctx.user.id != 710657087100944476:
            return
        if code[:3] == "```" and code[-3:] == "```":
            code = code[3:-3]
            if code[:2] == "py":
                code = code[2:]
        code = code.strip()

        await ctx.send(
            await aexec(
                code,
                {
                    "bot": self.bot,
                    "here": ctx.channel,
                    "message": ctx.message,
                    "reply": ctx.channel.fetch_message(
                        ctx.message.reference.message_id
                    ),
                },
            )
        )


def setup(bot: commands.Bot):
    bot.add_cog(InternalCog(bot))
