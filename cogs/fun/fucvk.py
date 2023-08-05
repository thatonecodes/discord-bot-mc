import discord
from discord.ext import commands
import traceback
import random
from config import icon, botname

class Fuvcker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def fucvk(self, ctx, member: discord.Member = None):
        try:
            urls = [
                "https://c.tenor.com/FmBSx-Wr1QgAAAAd/anime-redo-of-healer.gif",
                "https://i.pinimg.com/originals/f7/2f/1b/f72f1b87e0036e75dd6bcf2a3a1bb504.gif",
                "https://media.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif",
                "https://media.tenor.com/EW4YboL_nl0AAAAd/dio-brando-the-world.gif"
            ]
            random_url = random.choice(urls)
            if member is None:
                await ctx.send("Select a member ($fucvk @user)!")

            fucvkEmbed = discord.Embed(
                title="Oh my :scream: what are you-",
                description=f"{ctx.author.mention} fuc*s {member.mention}",
                color=discord.Colour.random()
            )
            fucvkEmbed.set_author(
                name=botname,
                icon_url=icon
            )
            fucvkEmbed.set_image(url=random_url)

            if random_url == "https://c.tenor.com/FmBSx-Wr1QgAAAAd/anime-redo-of-healer.gif":
                fucvkEmbed.set_footer(text="this is ptsd")
            elif random_url == "https://media.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif":
                fucvkEmbed.set_author(
                    name="NO",
                    icon_url=icon
                )
                fucvkEmbed.description = f"GO TO HORNY JAIL {ctx.author.mention}!"
            elif random_url == "https://media.tenor.com/EW4YboL_nl0AAAAd/dio-brando-the-world.gif":
                fucvkEmbed.title = "THE WORLD!"
                fucvkEmbed.description = f"GO TO HORNY JAIL {ctx.author.mention}!"
                fucvkEmbed.set_author(
                    name="no more horny",
                    icon_url=icon
                )
                fucvkEmbed.set_footer(text="DIO SAMA")
            
            await ctx.send(embed=fucvkEmbed)
        except Exception as e:
            traceback.print_exc()

async def setup(bot):
    await bot.add_cog(Fuvcker(bot))
