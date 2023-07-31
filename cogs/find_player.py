import discord
from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def example_command(self, ctx):
        await ctx.send('This is an example command!')

async def setup(bot):
    bot.add_cog(Template(bot))
