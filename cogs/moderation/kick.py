import discord
from discord.ext import commands
import traceback

class Kicker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            if member == None:
                await ctx.send("Select a user! (ex. $kick @user)!") 
                return
            elif member == ctx.message.author:
                await ctx.channel.send("You cannot kick yourself")
                return
            memberEmbed = discord.Embed(
                title="Kicked!",
                description=f"User {member} has been kicked for: {reason}",
                color=discord.Colour.random()
            )
            await member.kick(reason=reason)
            await ctx.send(embed=memberEmbed)
        except Exception as e:
            traceback.print_exc()

async def setup(bot):
    await bot.add_cog(Kicker(bot))
