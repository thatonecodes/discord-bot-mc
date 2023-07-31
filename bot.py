from discord.ext import commands
import discord
import config
from config import botname, icon
import os
import asyncio
import traceback



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        notfound = discord.Embed(
            title="Command not found!",
            description="Invalid command. Use $help to see all available commands.",
            color=discord.Color.red()
        )
        notfound.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        await ctx.send(embed=notfound)
    


async def loader():
    
    extensions = []
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog_name = filename[:-3]  # Remove the ".py" extension
            cog_path = f"cogs.{cog_name}"
            extensions.append(cog_path)
            print(extensions[0])
            for i in extensions:
                try:
                    await bot.load_extension(i)
                    print(f"Loaded cog: {i}")
                except discord.ext.commands.errors.ExtensionAlreadyLoaded:
                    pass
                except Exception as e:
                    print("ERROR")
                    traceback.print_exc()
                
token = config.TOKEN
async def main():
    async with bot:
        await loader()
        await bot.start(token)

asyncio.run(main())
