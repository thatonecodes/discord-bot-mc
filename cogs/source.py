import discord
from discord.ext import commands
from config import botname, icon
class sourceCode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def source(self, ctx):
        link = "https://github.com/thatonecodes/discord-bot-mc"
        sourceembed = discord.Embed(title="Source code for the bot.",
        description=f"The source code link is here: {link}",
        color=discord.Colour.random())
        sourceembed.set_author(
            name=botname,
            icon_url=icon
        )
        sourceembed.set_footer(text="make a pull request?")
        await ctx.send(embed=sourceembed)



async def setup(bot):
    await bot.add_cog(sourceCode(bot))