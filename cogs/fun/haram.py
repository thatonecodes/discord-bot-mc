import discord
from discord.ext import commands
import random
from config import icon, botname
import traceback
class Harami(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def haram(self, ctx, member: discord.Member = None):
        try:
            member = member or ctx.author.mention
            urls = ["https://media.tenor.com/usOrpkZk9QIAAAAM/haram-heisenberg.gif", "https://media.tenor.com/u5XBzG63c7YAAAAC/haram-andrew-tate.gif"]
            random_url = random.choice(urls)
            haramEmbed = discord.Embed(
                title="So NOT HALAL mode!",
                description=f"{ctx.author.mention} thinks {member.mention} is HARAM!",
                color=discord.Colour.random()
            )
            haramEmbed.set_author(
                name=botname,
                icon_url=icon
            )
            haramEmbed.set_footer(text="haram")
            haramEmbed.set_image(url=random_url)

            await ctx.send(embed=haramEmbed)   
        except Exception as e:
            traceback.print_exc()

async def setup(bot):
    await bot.add_cog(Harami(bot))
