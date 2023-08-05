import discord
from discord.ext import commands
from discord import app_commands

class template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="template", description="description", category="basic")
    async def template(self,interaction: discord.Interaction):
        await interaction.response.send_message("command")



async def setup(bot):
    await bot.add_cog(template(bot))