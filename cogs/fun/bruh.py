import discord
from discord.ext import commands
import random
from config import icon, botname

class Bruh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bruh(self, ctx):
        urls = ["https://us-tuna-sounds-images.voicemod.net/8657d656-18f5-470f-8303-c95f4f3fbfd6-1664164407190.jpg", "https://images.genius.com/12719860cb2edd87f3a7abea741a70ba.1000x1000x1.jpg", "https://static.truckersmp.com/images/vtc/logo/21823.1594940844.png", "https://i1.sndcdn.com/avatars-U3ir1j6Qhg3QxaII-zPG37Q-t500x500.jpg"]
        random_url = random.choice(urls)
        bruhEmbed = discord.Embed(
            title="bruh",
            description="bruh moment",
            color= discord.Colour.random()
        )
        bruhEmbed.set_author(
            name= botname,
            icon_url= icon
        )
        bruhEmbed.set_image(url=random_url)
        await ctx.send(embed=bruhEmbed)

async def setup(bot):
    await bot.add_cog(Bruh(bot))
