import discord
from discord.ext import commands
import random
import traceback
from config import icon, botname

class Finger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def star_finger(self, ctx, member: discord.Member = None):
        try:
            if member == None:
                await ctx.send("Choose a member($star_finger @user)!")
                return
            member = member
            
            finger = discord.Embed(
                title="GAH DAM - :point_right:",
                description=f"{ctx.author.mention} fingers {member.mention}!",
                color=discord.Colour.random()
            )

            urls = ["https://media.tenor.com/SqcvxN7Pfl0AAAAC/star-platinum.gif", "https://media.tenor.com/0m6Po4t45AoAAAAd/polnareff-polnareff-star-finger.gif", "https://media.tenor.com/RwQPqlGzyBcAAAAC/star-platinum-jojo.gif"]
            finger.set_image(url= random.choice(urls))

            finger.set_author(
                name=botname,
                icon_url=icon
            )
            await ctx.send(embed=finger)
        except Exception as e:
            traceback.print_exc()

async def setup(bot):
    await bot.add_cog(Finger(bot))
