import discord
from discord.ext import commands
import random
from config import icon, botname

class Slapper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        urls = ["https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif", "https://i.gifer.com/XaaW.gif", "https://c.tenor.com/noSQI-GitQMAAAAC/mm-emu-emu.gif", "https://i.imgur.com/fm49srQ.gif", "https://media.tenor.com/zYf61efRHoIAAAAd/slap-contest-hit-hard.gif"]
        random_urls = random.choice(urls)
        if member == None:
            await ctx.send("Select a user (ex $slap @user)!")
        slapembed = discord.Embed(
            title="SLAP!",
            description=f"{ctx.author.mention} slaps {member.mention}!",
            color=discord.Colour.random()
        )
        slapembed.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        slapembed.set_footer(text="ouch")
        slapembed.set_image(url=random_urls)
        await ctx.send(embed=slapembed)

async def setup(bot):
    await bot.add_cog(Slapper(bot))
