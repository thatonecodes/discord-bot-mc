import discord
from discord.ext import commands
import random
from config import icon, botname
import traceback

class HalalMode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def halal(self, ctx, member: discord.Member = None):
        try:
            member = member or ctx.author.mention
            urls = ["https://media.tenor.com/pzIefmS6xs4AAAAM/ayaan-ayaanus.gif", "https://media.tenor.com/L2n8XN3fvQQAAAAd/halal.gif", "https://media.tenor.com/Ma1qzPPhgHkAAAAM/breaking-bad-halal.gif"]
            random_url = random.choice(urls)
            halalEmbed = discord.Embed(
                title="So Halal mode!",
                description=f"{ctx.author.mention} thinks {member.mention} is halal!",
                color=discord.Colour.random()
            )
            halalEmbed.set_author(
                name=botname,
                icon_url=icon
            )
            halalEmbed.set_footer(text="halal")
            halalEmbed.set_image(url=random_url)

            await ctx.send(embed=halalEmbed)   
        except Exception as e:
            traceback.print_exc()
async def setup(bot):
    await bot.add_cog(HalalMode(bot))
