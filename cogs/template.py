import discord
from discord.ext import commands

class template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def template(self, ctx):
        await ctx.send("test")


async def setup(bot):
    await bot.add_cog(template(bot))