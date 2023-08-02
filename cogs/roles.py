import discord
from discord.ext import commands
from config import defaultgulidID, botname, icon

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def roles(self, ctx):
        try:
            MAIN_GUILD = self.bot.get_guild(defaultgulidID)  # Use default guild id
            roles = MAIN_GUILD.roles
            role1 = discord.utils.get(roles, name="gigachad clan")
            role2 = discord.utils.get(roles, name="the duhjer clan")
            role3 = discord.utils.get(roles, name="the anti-duhjer clan")
            role4 = discord.utils.get(roles, name="neutral")
            messageembed = discord.Embed(
                title="Role Reactions :boom:",
                description="""If you'd like to join a team, react to one of the emojis, down below, starting with\n gigachad clan: :sunglasses: | the duhjer clan :grimacing: | the anti-duhjer clan :white_check_mark: | neutral :flag_ch:""",
                color=discord.Colour.random()
            )
            messageembed.set_author(
                name=botname,
                icon_url=icon
            )
            messageembed.set_footer(text="you can only choose one team!")
            message = await ctx.send(embed=messageembed)
            emoji1 = '😬'
            emoji2 = '😎'
            emoji3 = '✅'
            emoji4 = '🇨🇭'
            await message.add_reaction(emoji1)
            await message.add_reaction(emoji2)
            await message.add_reaction(emoji3)
            await message.add_reaction(emoji4)
            
            def check(payload):
                return payload.user_id == ctx.author.id and str(payload.emoji) in [emoji1, emoji2, emoji3, emoji4] and payload.message_id == message.id
            
            payload = await self.bot.wait_for("raw_reaction_add", timeout=180, check=check)
            member = MAIN_GUILD.get_member(payload.user_id)
            if member is not None:
                emoji = str(payload.emoji)
                if emoji == emoji1:
                    await member.add_roles(role1)
                elif emoji == emoji2:
                    await member.add_roles(role2)
                elif emoji == emoji3:
                    await member.add_roles(role3)
                elif emoji == emoji4:
                    await member.add_roles(role4)
                await ctx.send("Added role!")
           
        except Exception as e:
            print("Error:", e)


async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))