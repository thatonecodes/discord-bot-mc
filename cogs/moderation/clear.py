import discord
from discord.ext import commands
import traceback

class ClearMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        try:
            if 1 <= amount <= 100:
                deleted = await ctx.channel.purge(limit=amount + 1)
                await ctx.send(f"Deleted {len(deleted) - 1} message(s)!")
            elif 100 <= amount <= 1000:
                message = await ctx.send("Number is over 100, may take a while.")
                deleted = await ctx.channel.purge(limit=amount + 1)
                await ctx.send(f"Deleted {len(deleted) - 1} message(s)!")
            elif 1000 <= amount <= 10000:
                await ctx.send("Cannot delete more than 1000!")
                return
            else:
                await ctx.send("Enter a number/ errno.")
        except Exception as e:
            traceback.print_exc()



async def setup(bot):
    await bot.add_cog(ClearMessages(bot))
