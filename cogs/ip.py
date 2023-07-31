import discord
from discord.ext import commands
from config import minecraftserverip, minecraftserverport, botname, icon

class IpGetter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ip(self, ctx, ip: str = minecraftserverip, port: str = minecraftserverport):
        ipEmbed = discord.Embed(
            title="Server IP and port :desktop:",
            description=f"IP: {ip} \n Port: {port}",
            color=discord.Colour.random()
        )
        ipEmbed.set_author(
            name= botname,
            icon_url= icon
        )
        await ctx.send(embed=ipEmbed)

async def setup(bot):
    await bot.add_cog(IpGetter(bot))