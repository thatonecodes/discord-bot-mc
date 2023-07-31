import discord
from discord.ext import commands
from config import icon, botname
import random

class LowTierGod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ltg(self, ctx):
        urls = ["https://media.tenor.com/b5uy31YIxE8AAAAd/ltg-low-tier-god.gif", "https://media.tenor.com/2wJ6I1I_tqEAAAAC/ltg-low-tier-god.gif", "https://media.tenor.com/SWRwTE3J_fYAAAAd/ltg.gif", "https://media.tenor.com/JHRBvg3bY68AAAAd/low-tier-god-gtab.gif", "https://media.tenor.com/rtFcrfD0FC8AAAAd/low-tier-god-your-life-has-zero-purpose.gif", "https://media.tenor.com/OGRRT-SrTCIAAAAM/you-should-treat-yourself-now.gif"]
        ltgembed=discord.Embed(
            title="LTG SAYS:",
            description="you should :zap: :zap: :zap: yourself NOW!",
            color=discord.Colour.random()
        )
        ltgembed.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        random_url = random.choice(urls)
        ltgembed.set_image(url=random_url)
        if random_url == "https://media.tenor.com/OGRRT-SrTCIAAAAM/you-should-treat-yourself-now.gif":
            ltgembeds=discord.Embed(
            title="LTG SAYS:",
            description="you should :hearts::hearts::hearts: yourself now!",
            color=discord.Colour.random()
        )
            ltgembeds.set_image(url="https://media.tenor.com/OGRRT-SrTCIAAAAM/you-should-treat-yourself-now.gif")

            ltgembeds.set_author(
                name=f"{botname}",
                icon_url=f"{icon}"
            )
            ltgembeds.set_footer(text="thanks!")
            await ctx.send(embed=ltgembeds)
        else:
            ltgembed.set_footer(text="just kidding don't actually do that..(pls)")
            await ctx.send(embed=ltgembed)

async def setup(bot):
    await bot.add_cog(LowTierGod(bot))
