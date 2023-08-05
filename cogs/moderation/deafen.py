import discord
from discord.ext import commands
import traceback

class Deafener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def deafen(self, ctx, member: discord.Member):
        voice_state = member.voice
        try:
            memberEmbed = discord.Embed(
                title="Deafened",
                description=f":headphones: User {member.mention} has been server deafened.",
                color=discord.Colour.random()
            )
            if member == ctx.message.author and ctx.message.author.voice == True:
                await ctx.message.author.edit(deafen=True)
                await ctx.send(embed=memberEmbed)
            if voice_state is None:
                return await ctx.send('The user needs to be in a voice channel to use this command!')
            if voice_state is not None:
                await member.edit(deafen=True)
                await ctx.send(embed=memberEmbed)
            else:
                print("untrue")

    
        except Exception as e:
            traceback.print_exc()
            await ctx.send("something went wrong..")


async def setup(bot):
    await bot.add_cog(Deafener(bot))
