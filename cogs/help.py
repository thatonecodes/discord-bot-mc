import discord
from discord.ext import commands
from config import botname, icon
import traceback

class Helper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        try:
            helptext = "```"
            for command in self.bot.commands:
                helptext+=f"{command}\n"
            helptext+="```"

            helpcmds = discord.Embed(
                title=f"Help & all commands!",
                description=f"The commands are ($): \n{helptext}",
                color=discord.Colour.random()
            )
            helpcmds.add_field(name="Usage", value="To use the bot, simply put a $ in front of the command. (ex $help, $rules)", inline= False)
            helpcmds.set_author(
                name=f"{botname}",
                icon_url=f"{icon}"
            )
            helpcmds.set_footer(text="created by dionednrg")
            await ctx.send(embed=helpcmds)
        except Exception as e:
            traceback.print_exc()
            print("bruh")


async def setup(bot):
    await bot.add_cog(Helper(bot))