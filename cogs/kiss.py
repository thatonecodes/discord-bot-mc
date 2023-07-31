import discord
from discord.ext import commands
from config import botname, icon
import random
import traceback
class KissMen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        try:
            urls = ["https://media.giphy.com/media/l4FsKa1n9fyStiwZW/giphy.gif", "https://c.tenor.com/wDYWzpOTKgQAAAAC/anime-kiss.gif", "https://media.tenor.com/217aKgnf16sAAAAC/kiss.gif", "https://c.tenor.com/el8DHxNp9IsAAAAC/kiss-anime-love.gif"]
            random_url = random.choice(urls)
            if member == None:
                await ctx.send("Select a user (ex. $kiss @user)!")
            
            kissEmbed = discord.Embed(
                title=":heart: wow!",
                description=f"{ctx.author.mention} kissed {member.mention}",
                color=discord.Colour.random()
            )
            kissEmbed.set_image(url=random_url)
            kissEmbed.set_footer(text="nice")
            kissEmbed.set_author(
                name=f"{botname}",
                icon_url=f"{icon}"
            )
            await ctx.send(embed=kissEmbed)
        except Exception as e:
            traceback.print_exc()

async def setup(bot):
    await bot.add_cog(KissMen(bot))
