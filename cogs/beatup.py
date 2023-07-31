import discord
from discord.ext import commands
import random
from config import botname,icon

class Beater_upper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def beatup(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        urls = ["https://media.tenor.com/qKTBsktfhSgAAAAd/punch-blue-hoodie.gif", "https://media.tenor.com/DE8TGcQUcMwAAAAC/rapid-punch-twinzero.gif", "https://media.tenor.com/ZXM8sTlvCnQAAAAM/promethozeen.gif", "https://media.tenor.com/LGCkjHzWvecAAAAd/beating-up-beat-up.gif"]
        url_random = random.choice(urls)
        beat_up_embed = discord.Embed(
            title="Fight back, FIGHT BACK!",
            description=f"{ctx.author.mention} beats up {member.mention}",
            color=discord.Colour.random()
        )
        beat_up_embed.set_image(url=url_random)
        beat_up_embed.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        beat_up_embed.set_footer( text="he ded :skull:")
        
        await ctx.send(embed=beat_up_embed)

async def setup(bot):
    await bot.add_cog(Beater_upper(bot))
