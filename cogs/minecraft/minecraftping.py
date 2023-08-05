import discord
from discord.ext import commands
from config import linkMC, botname, icon
from bs4 import BeautifulSoup
import traceback
import aiohttp
import asyncio
class MinecraftPinger(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.offline_message_sent = False

        async def get_page_source(self, ctx):
            try:     
                while True:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(linkMC) as response:
                            if response.status == 200:
                                content = await response.text()
                                soup = BeautifulSoup(content, "html.parser")
                                var = soup.find("span", {"id": "statusdetail-ajax"})
                                Ooops = var.contents
                                if Ooops == ['Offline']:
                                    print(Ooops)
                                    serveroffline = discord.Embed(
                                        title="Server Offline..",
                                        description="Currently, the server is offline.. it will be online soon? (you will be pinged)",
                                        color=discord.Colour.random()
                                    )
                                    serveroffline.set_author(name=botname, icon_url= icon)
                                    if self.offline_message_sent == False:
                                        await ctx.send(embed=serveroffline)
                                        self.offline_message_sent = True
                                else:
                                    print("serveronline")
                                    allowed_mentions = discord.AllowedMentions(everyone = True)
                                    await ctx.send(content = "@everyone", allowed_mentions = allowed_mentions)
                                    serveronline = discord.Embed(
                                        title="SERVER ONLINE!",
                                        description=f"The minecraft server is online!",
                                        color=discord.Colour.random()
                                    )
                                    serveronline.set_author(
                                        name=botname,
                                        icon_url= icon
                                    )
                                    serveronline.set_footer(text="go play")
                                    await ctx.send(embed=serveronline)
                                    break
                    
                    await asyncio.sleep(10)

            except Exception as e:
                 traceback.print_exc()


        @commands.has_permissions(manage_messages = True)
        @commands.command()
        async def pingserver(self, ctx):
            try:
            # Call the web scraping function when the command is invoked
                
                await self.get_page_source(ctx)
            except Exception as e:
                traceback.print_exc()





async def setup(bot):
    await bot.add_cog(MinecraftPinger(bot))