import discord 
from discord.ext import commands
from config import botname, icon

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        
    @commands.command()
    async def rules(self, ctx):
        try:
            rules = discord.Embed(
            title="Rules:",
            description="""Read the fucking rules: \n1. no skybases :neutral_face: \n2. declare war before attacking or get timeout from server :cold_face: \n3. no offline raids (this is not rust):face_with_raised_eyebrow: \n4. no underground bases(unfindable) :man_gesturing_no: \n5. no attacking during grace/peace periods :attack: \n6. no going onto claimed land in peace time(unless you're visiting) :peace: \n7. be respectful. dont harass too much or you will get a timeout :clock: \n8. no hacking/cheating/duping/exploiting/bypassing (includes xray) :computer: \n9. no lag machines :lab_coat: \n10. just a bit of trolling :troll:
            """,
            color=discord.Colour.random(),
        )
            image = "https://media.tenor.com/gbAllo1T0BAAAAAd/hello-anime-rules.gif"
            rules.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
            await ctx.send(image)
            await ctx.send(embed=rules)

        except Exception as e:
            print("bruh")

async def setup(bot):
    await bot.add_cog(Rules(bot))
