import discord
from discord.ext import commands
import requests
import base64
import io
from PIL import Image
import traceback
from config import icon, botname, minecraftserverip, minecraftserverport
import os


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
                players_online = data["players"]["online"]
                player_info = "No players online"
                max_players = data["players"]["max"]
                version = data["version"]
                is_online = data["online"]
                if icon is not None:
                    image_icon = data["icon"]

                base64_data = image_icon.replace("data:image/png;base64,", "")

                # Decode Base64 and create an image from it
                image_data = base64.b64decode(base64_data)
                image = Image.open(io.BytesIO(image_data))

                image_path = "decoded_image.png"
                image.save(image_path)

                if "software" in data:
                    software = data["software"]

                else:
                    software = "Unknown"

                information = data["motd"]["clean"]

                minecraft_embed = discord.Embed(
                    title=f"Minecraft Server Information for {ip}",
                    description=f"""Server IP: {ip_address}:{port}
                    Players Online: {players_online}/{max_players}
                    Version: {version}
                    Online: {is_online}
                    Software: {software}
                    Description: {' '.join(str(i) for i in information)}""",
                    color=discord.Colour.random()
                )
                minecraft_embed.set_author(
                    name=botname,
                    icon_url=icon
                )
                minecraft_embed.set_footer(text="credit to mcsrvstat for the API")
                with open(image_path, "rb") as f:
                    picture = discord.File(f)
                    await ctx.send(file=picture)
                    await ctx.send(embed=minecraft_embed)
                os.remove(image_path)

        except KeyError:
            traceback.print_exc()
            print("Failed to retrieve server information.")
            await ctx.send("Invalid IP, please try again!")

        except Exception as e:
            traceback.print_exc()
            print("Error occurred while fetching server information.")

async def setup(bot):
    await bot.add_cog(MinecraftServer(bot))
