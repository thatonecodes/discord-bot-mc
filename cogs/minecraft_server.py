import discord
from discord.ext import commands
import requests
import base64
import io
from PIL import Image
import traceback
from config import icon, botname, minecraftserverip, minecraftserverport
import os
import textwrap


class MinecraftServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def minecraft_server(self, ctx, ip: str = minecraftserverip + ":" + minecraftserverport):
    #start using the minecraft_server api to interact with servers
        try:
            minecraft_server_url = f"https://api.mcsrvstat.us/2/{ip}"
            response = requests.get(minecraft_server_url)
            data = response.json()

            if "ip" in data and "port" in data:
                ip_address = data["ip"]
                port = data["port"]
                players_online = "No players online. Server Offline."
                max_players = "60"
                is_online = data["online"]
                version = "1.19.2"
                software = "Forge"
                information = "None"
                image_icon = ""
                ping = data["debug"]["ping"]
                player_list_unpacked = "Server Offline."
                if is_online is not False:
                    version = data["version"]
                    players_online = data["players"]["online"]
                    max_players = data["players"]["max"]
                    image_icon = data["icon"]
                    player_list = "No players Online"
                    player_list_unpacked = "No players online."
                    if players_online != 0:
                        player_list = data["players"]["list"]
                        player_list_unpacked = " ".join(str(f) for f in player_list)

                    base64_data = image_icon.replace("data:image/png;base64,", "")

                    # Decode Base64 and create an image from it
                    image_data = base64.b64decode(base64_data)
                    image = Image.open(io.BytesIO(image_data))

                    image_path = "decoded_image.png"
                    image.save(image_path)

                    information = data["motd"]["clean"]

                if "software" in data:
                    software = data["software"]

                else:
                    software = "Forge (default)"
                description_triple = f"""
                    Server IP: {ip_address}:{port}
                    Players Online: {players_online}/{max_players}
                    Player List: {player_list_unpacked}
                    Version: {version}
                    Online: {is_online}
                    Software: {software}
                    Ping: {ping}
                    Description: {' '.join(str(i) for i in information)}"""
                description_dedent =textwrap.dedent(description_triple)
                

                minecraft_embed = discord.Embed(
                    title=f"Minecraft Server Information for {ip}",
                    description= description_dedent,
                    color=discord.Colour.random()
                )
                minecraft_embed.set_author(
                    name=botname,
                    icon_url=icon
                )
                minecraft_embed.set_footer(text="credit to mcsrvstat for the API")
                if image_icon != "":
                    with open(image_path, "rb") as f:
                        picture = discord.File(f)
                        await ctx.send(file=picture)
                        await ctx.send(embed=minecraft_embed)
                    os.remove(image_path)
                else:
                    await ctx.send("No Icon or offline.")
                    await ctx.send(embed=minecraft_embed)

        except KeyError:
            traceback.print_exc()
            print("Failed to retrieve server information.")
            await ctx.send("Invalid IP, please try again!")

        except Exception as e:
            traceback.print_exc()
            print("Error occurred while fetching server information.")
            await ctx.send("error..")

async def setup(bot):
    await bot.add_cog(MinecraftServer(bot))
