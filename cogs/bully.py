import discord
from discord.ext import commands
import random
from config import botname, icon

class Bullier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bully(ctx, member: discord.Member = None):
        urls = []
        random_urls = random.choice(urls)
        if member == None:
            await ctx.send("Select a user (ex $bully @user)!")
        bullyembed = discord.Embed(
            title="A bully!",
            description=f"{ctx.author.mention} bullies {member.mention}!",
            color=discord.Colour.random()
        )
        bullyembed.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        bullyembed.set_footer(text="do not try this at home")
        bullyembed.set_image(url=random_urls)
        await ctx.send(embed=bullyembed)


async def setup(bot):
    await bot.add_cog(Bullier(bot))
