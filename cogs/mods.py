import discord
from discord.ext import commands
from config import modstext, icon, botname

class ModLoader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def mods(self, ctx, mods = modstext):
        Modembed = discord.Embed(
            title="Mods",
            description=f"{mods}",
            color=discord.Colour.random()
        )
        Modembed.set_author(
            name= botname,
            icon_url=icon
        )
        await ctx.send(embed=Modembed)

async def setup(bot):
    await bot.add_cog(ModLoader(bot))