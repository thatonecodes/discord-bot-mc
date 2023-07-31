import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from config import icon, botname
import traceback


class GetSkin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def skin(self, ctx, player):
        try:
            player = player
            if player == None:
                await ctx.send("Please select a player! (ex. $skin [player])")
            url = f"https://minecraftuuid.com/?search={player}"
            get_url = requests.get(url)
            soup = BeautifulSoup(get_url.content, "html.parser")
            input_field = soup.find("input", {"type": "text", "class": "Form-Control", "placeholder": "Trimmed UUID"})
            uuid_value = input_field.get("value")
            skin_image_url = f"https://crafatar.com/renders/body/{uuid_value}"
            name_mc_url = f"https://namemc.com/profile/{player}.1"
            skinEmbed = discord.Embed(
                title=f"Skin of player: {player}",
                description="The player's skin is shown below.",
                color=discord.Colour.random(),
                url= name_mc_url
            )
            skinEmbed.set_image(url=skin_image_url)
            skinEmbed.set_author(
                name=f"{botname}",
                icon_url=f"{icon}"
            )
            skinEmbed.set_footer( text="* credit to namemc and crafatar for API and links")
            await ctx.send(embed=skinEmbed)

        except AttributeError:
            await ctx.send("Invalid user! Please try again.")
            traceback.print_exc()
        except Exception as e:
            print("execption")
            traceback.print_exc()
            await ctx.send("An error occurred.")

async def setup(bot):
    await bot.add_cog(GetSkin(bot))
