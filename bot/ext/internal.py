from nextcord.ext import commands
from aioconsole import aexec


class InternalCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
    
    @commands.command()
    async def eval(self, ctx: commands.Context, *, code: str) -> None:
        if ctx.author.id != 710657087100944476:
            return
        if code[:3] == "```" and code[-3:] == "```":
            code = code[3:-3]
            if code[:2] == "py":
                code = code[2:]
        code = code.strip()
        ref = ctx.message.reference
        reply = None
        if ref is not None:
            reply = ctx.channel.fetch_message(ref.message_id)
        await ctx.message.delete()
        await ctx.send(await aexec(code, {"bot": self.bot, "here": ctx.channel, "message": ctx.message, "reply": reply}))

def setup(bot: commands.Bot):
    bot.add_cog(InternalCog(bot))
