import discord
from discord.ext import commands
import traceback

class ClearMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(ctx, amount: int):
        try:
            if 1 <= amount <= 100:
                deleted = await ctx.channel.purge(limit=amount + 1)
                await ctx.send(f"Deleted {len(deleted) - 1} message(s)!")
            else:
                await ctx.send("Please provide a number between 1 and 100.")
        except Exception as e:
            traceback.print_exc()


async def setup(bot):
    await bot.add_cog(ClearMessages(bot))
