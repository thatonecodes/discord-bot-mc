import discord
from discord.ext import commands
from config import mapimagelink, maplink
class Mapper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def map(self, ctx):
        image = mapimagelink
        maplinker = f"The link to access the dynmap is: {maplink}"
        await ctx.send(maplinker)
        await ctx.send(image)

async def setup(bot):
    await bot.add_cog(Mapper(bot))