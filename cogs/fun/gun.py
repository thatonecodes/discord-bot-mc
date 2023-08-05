import discord
from discord.ext import commands
import random
from config import icon, botname

class GunCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def gun(self, ctx, member: discord.Member = None):
        urls = ["https://media.tenor.com/2p9YmPClM0oAAAAC/justified-gun-spinning.gif", "https://media.tenor.com/AO_oFEKPj4AAAAAC/gun-firing.gif", "https://media.tenor.com/cKFZd3_-4YcAAAAd/call-of-duty-revolver.gif", "https://static.wikia.nocookie.net/valorant/images/2/23/GoldenGun.png/revision/latest?cb=20210122000812", "https://media.tenor.com/opl-nN4yPRwAAAAd/valorant-gun.gif"]
        random_url = random.choice(urls)
        gunEmbed = discord.Embed(
            title="G U N",
            description= ":gun:",
            color=discord.Colour.random()
        )
        gunEmbed.set_author(
            name= botname,
            icon_url= icon
        )
        gunEmbed.set_image(url=random_url)
        await ctx.send(embed=gunEmbed)

async def setup(bot):
    await bot.add_cog(GunCommand(bot))
