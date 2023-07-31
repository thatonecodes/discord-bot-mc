import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random
import traceback
from config import icon, botname


class Stander(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def stand(self, ctx):
        try:
            loading_msg = await ctx.send("Parsing stands, please wait...")
            url = "https://jojowiki.com/List_of_Stands"
            get_url =  requests.get(url)
            soup = BeautifulSoup(get_url.content, "html.parser")
            all_stands = []
            all_links = []
            formatted_links = []
            stands = soup.find_all("div", class_="charbox")
            for stand in stands:
                char_img = stand.find("img")["src"].strip()
                char_src = stand.find("a")["href"].strip()
                char_name = stand.find("div", class_="charname").text.strip()
                char_stand = stand.find("div", class_="charstand").text.strip()
                all_stands.append((char_name, char_stand))
                all_links.append((char_img,char_src))

            for img, src in all_links:
                if "%27" in src:
                    formatted_src1 = src.replace("%27", "'").replace("_", " ")
                    formatted_src = formatted_src1.lstrip('/').replace('_', ' ')
                elif "%C3%" in src:
                    formatted_src1 = src.replace("%C3%", "'").replace("_", " ")
                    formatted_src = formatted_src1.lstrip('/').replace('_', ' ')
                elif "%26" in src:
                    formatted_src1 = src.replace("%26", "&").replace("_", " ")
                    formatted_src = formatted_src1.lstrip('/').replace('_', ' ')
                else:
                    formatted_src = src.lstrip('/').replace('_', ' ')
                formatted_links.append((formatted_src, img))

            random_stand_data = []
            random_stand = random.choice(all_stands)
            linker = random_stand[0].replace(" ", "_")
            src = f"https://jojowiki.com/{linker}"
            for formatted_src, img in formatted_links:
                if random_stand[0] == formatted_src:
                    random_stand_data.append((random_stand[0], random_stand[1], img, src))
                    print("success")
                    break
            else:
                await loading_msg.edit(content="No stand found for the given name. Rerun Command!")
                return


            if len(random_stand_data) > 0:
                name, stand, img, stand_src = random_stand_data[0]
                jojoStand=discord.Embed(
                    title=f"Your stand is:\n{name}",
                    description=f"{stand}",
                    url=f"{stand_src}",
                    color=discord.Colour.random()
                )
                jojoStand.set_author(
                    name=f"{botname}",
                    icon_url=f"{icon}"
                )
                jojoStand.set_image(url=f"{img}")
                jojoStand.set_footer(text="iS tHaT a jOjO rEfErEnCe!1!1!!")
                await ctx.send(embed=jojoStand)
            await loading_msg.edit(content="Stand comparison completed!")

        except requests.exceptions.RequestException as e:
            print("Error fetching the URL:", e)
        except Exception as e:
            traceback.print_exc()
            errorEmbed = discord.Embed(
                title="Error!",
                description="An error occured!",
                color=discord.Color.red()
            )
            errorEmbed.set_author(
                name=f"{botname}",
                icon_url=f"{icon}"
            )
            await ctx.send(embed=errorEmbed)


#DO THIS FASTER !!!!!
async def setup(bot):
    await bot.add_cog(Stander(bot))
