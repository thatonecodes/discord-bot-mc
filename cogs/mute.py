import discord
from discord.ext import commands
import traceback

class Muter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        try:
            voice_state = member.voice

            if not ctx.author.voice:
                return await ctx.send("You need to be in a voice channel to use this command.")

            if voice_state is None:
                return await ctx.send("The user needs to be in a voice channel to use this command.")

            await member.edit(mute=True)

            member_embed = discord.Embed(
                title="Muted",
                description=f":microphone: User {member.mention} has been server muted.",
                color=discord.Colour.random()
            )
            await ctx.send(embed=member_embed)

        except Exception as e:
            traceback.print_exc()
            await ctx.send("Something went wrong..")

async def setup(bot):
    await bot.add_cog(Muter(bot))
