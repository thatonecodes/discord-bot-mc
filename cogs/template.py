import discord
from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bruh():
        print("bruh")


async def setup(bot):
    await bot.add_cog(Template(bot))