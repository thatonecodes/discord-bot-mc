import discord
from discord.ext import commands
import traceback

class Banner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member,*, reason = None):
        try:
            if member == None:
                await ctx.send("Select a user! (ex. $ban @user)!") 
                return
            elif member == ctx.message.author:
                await ctx.channel.send("You cannot ban yourself")
                return
            if reason == None:
                reason = "(no reason provided)"
            messageembed = discord.Embed(
                title= "banned",
                description=f"{member} was banned for: {reason}",
                color=discord.Colour.random()
            )
            messageembed.set_footer(text="ban hammer :hammer:")
            await member.ban(reason=reason)
            await ctx.send(embed=messageembed)
        except Exception as e:
            print("error")
            traceback.print_exc()

async def setup(bot):
    await bot.add_cog(Banner(bot))
