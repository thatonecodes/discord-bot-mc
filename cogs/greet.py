import discord
from discord.ext import commands
import random
from config import botname, icon

class Greeter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def greet(self, ctx, member: discord.Member = None):
        member = member
        urls = ["https://c.tenor.com/FMpLzF4UJhwAAAAC/kisumi-wave.gif", "https://media.tenor.com/47GM87fDYNYAAAAC/shouko-nishimiya-bow.gif", "https://media.giphy.com/media/AFdcYElkoNAUE/giphy.gif", "https://i.gifer.com/origin/55/55f1f99ec4fceab6af26e290a9bccdcd_w200.gif"]
        random_urls = random.choice(urls)
        
        if member == ctx.author:
            greetEmbed = discord.Embed(
                title="It's okay..",
                description="I feel the same way manye..",
                color=discord.Colour.blue()
            )
            greetEmbed.set_image(url="https://media.tenor.com/6guCYKvjVcAAAAAd/sad-sad-spongebob-gif.gif")
            greetEmbed.set_footer(text="feelsbadman")
        elif member == None:
            await ctx.send("Select a user(ex $greet @user)!")
        else:
            greetEmbed = discord.Embed(
                title="Hi, how are ya?",
                description=f"{ctx.author.mention} greets {member.mention}!",
                color=discord.Colour.random()
            )
            # Select a random URL from the list of URLs
            greetEmbed.set_image(url=random_urls)
            greetEmbed.set_footer(text="wholesome moment")

        greetEmbed.set_author(
            name=botname,
            icon_url=icon
        )
        
        
        await ctx.send(embed=greetEmbed)

async def setup(bot):
    await bot.add_cog(Greeter(bot))
