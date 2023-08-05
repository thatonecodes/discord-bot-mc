import discord
from discord.ext import commands
from config import botname, icon
import traceback
import os
class Helper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.commands = commands

    @commands.command()
    async def help(self, ctx):
        try:
            bot = self.bot
            helptext = "```"
            for command in self.bot.commands:
                helptext+=f"{command}\n"
            helptext+="```"
            
            basiccommands = []
            funcommands = []
            minecraftcommands = []
            peacetimecmds = []
            moderationcommands = []
            automationcmds = []

            #get PEACETIME CMDS
            rules_cog = bot.get_cog("PeaceTimer")
            commands_list = rules_cog.get_commands()
            admin_commands = ["$declarewaroverrule", "$warmodeactive", "$warmodeoff", "$aborttimer"]
            for command in commands_list:
                peacetimecmds.append(f"${command}")
                print(command)
            for command_name in admin_commands:
                if command_name in peacetimecmds:
                    peacetimecmds = [f"{command} (Admin Command)" if command in admin_commands else f"{command}" for command in peacetimecmds]
                    print(peacetimecmds)
                            
            #get BOTLOGIN CMDS
            automation_cog = bot.get_cog("BotLogin")
            automation_command_name = automation_cog.get_commands()
            for commands in automation_command_name:
                automationcmds.append(f"${commands}")
                print(command)


            for _, _, filenames in os.walk("./cogs/moderation"):
                for filename in filenames:
                    if filename.endswith(".py"):
                        moderation_filename = filename[:-3]
                        moderationcommands.append(f"${moderation_filename}")
                        print(moderationcommands)

            for _, _, filenames in os.walk("./cogs/fun"):
                for filename in filenames:
                    if filename.endswith(".py"):
                        fun_filename = filename[:-3]
                        funcommands.append(f"${fun_filename}")
                        print(funcommands)

            for _, _, filenames in os.walk("./cogs/basic"):
                for filename in filenames:
                    if filename.endswith(".py"):
                        basic_name = filename[:-3]
                        basiccommands.append(f"${basic_name}")
                        print(basiccommands)

            for _, _, filenames in os.walk("./cogs/minecraft"):
                for filename in filenames:
                    if filename.endswith(".py"):
                        basic_name = filename[:-3]
                        minecraftcommands.append(f"${basic_name}")
                        if "$peacetime".lower() in minecraftcommands:
                            minecraftcommands.remove("$peacetime")
                        print(minecraftcommands)
                    
                

            helpcmds = discord.Embed(
                title=f"Help & all commands!",
                color=discord.Colour.random()
            )
            helpcmds.add_field(name="BASIC", value=f"```{', '.join(basiccommands)}```", inline=False)
            helpcmds.add_field(name="FUN", value=f"```{', '.join(funcommands)}```", inline=False)
            helpcmds.add_field(name="MINECRAFT", value=f"```{', '.join(minecraftcommands)}```", inline=False)
            helpcmds.add_field(name="PEACETIME(Minecraft)", value=f"```{', '.join(peacetimecmds)}```", inline=False)
            helpcmds.add_field(name="MODERATION", value=f"```{', '.join(moderationcommands)}```", inline=False)
            helpcmds.add_field(name="AUTOMATION(Admin)", value=f"```{', '.join(automationcmds)}```", inline=False)

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