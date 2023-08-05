import discord
from discord.ext import commands
from config import icon, botname
import random
class Killer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def kill(self, ctx, member: discord.Member = None):
        member = member
        if member == None:
            await ctx.send("Select a member!(ex. kill @user)")
            return
        urls = ["https://media.tenor.com/uLq-U2cHgOgAAAAC/point-gun-shoot.gif", "https://i.pinimg.com/originals/04/ef/fa/04effa171ee2ecee7418eb98016d433a.gif", "https://media.tenor.com/u3azQsuPm0QAAAAC/die-gun.gif", "https://media.tenor.com/R9xae2ktRN8AAAAC/bang-deanwinchester.gif", "https://media.tenor.com/Y_inndSQYP8AAAAC/jojo-king-crimson.gif", "https://media.tenor.com/r-mjvq-uBUkAAAAd/gold-experience-requiem-diavolo-jjba.gif"]
        random_url = random.choice(urls)
        killembed=discord.Embed(
            title=":knife: :drop_of_blood: bruh dead",
            description=f"{ctx.author.mention} kills {member.mention}!",
            color=discord.Colour.random()
        )
        killembed.set_image(url=random_url)
        killembed.set_footer(text="just kidding chads never die")
        killembed.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        
        
        await ctx.send(embed=killembed)
async def setup(bot):
    await bot.add_cog(Killer(bot))
