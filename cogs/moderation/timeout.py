import discord
from discord.ext import commands
import datetime
import traceback

class TimeoutTime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: discord.Member, time, reason=None):
        try:
            if member == None:
                await ctx.send("Select a user! (ex. $timeout @user)!") 
                return
            elif member == ctx.message.author:
                await ctx.channel.send("You cannot timeout yourself!")
                return
            if "h" in time:
                time = time.replace("h","")
                print(time)
            if "d" in time:
                time = time.replace("d","")
                print(time)
            
            await member.timeout(datetime.timedelta(hours=int(time)), reason=reason)
            

            await member.timeout(datetime.timedelta(days=int(time)), reason=reason)
            embed = discord.Embed(title="Timed Out!",
                    description=f":white_check_mark: {member.name} has been successfully timed out.",
                    color=discord.Colour.random()
                    )
            if reason is not None:
                embed = discord.Embed(
                    title="Timed Out!",
                    description=f":white_check_mark: {member.name} has been successfully timed out for the reason: {reason}.",
                    color=discord.Colour.random())
            await ctx.send(embed=embed)
        
        except Exception as e:
            traceback.print_exc()

async def setup(bot):
    await bot.add_cog(TimeoutTime(bot))
