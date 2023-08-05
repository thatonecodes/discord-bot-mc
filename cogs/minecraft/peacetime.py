from datetime import datetime
from pytz import timezone
import discord
from discord.ext import commands
import asyncio
from config import botname, icon
import traceback

class PeaceTimer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tz = timezone('EST')
        self.time = datetime.now(self.tz) 
        self.countdown_time = 0
        self.resettime = 0
        self.resettime_task = None
        self.countdown_task = None
        self.warmode = False
        self.startingseconds = None

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def settimer(self, ctx, Startseconds: str):
        try:
            if Startseconds == "1d".lower():
                Startseconds = 86400
            if Startseconds == "2d".lower():
                Startseconds = 86400 * 2
            if int(Startseconds) <= 0:
                await ctx.send("Please enter a positive number for the countdown.")
                return
            self.startingseconds = int(Startseconds)
            self.countdown_time = int(Startseconds)
            message = await ctx.send(f"Countdown started for {self.countdown_time} seconds!")
                
                

            self.countdown_task = asyncio.create_task(self.countdown(ctx, message))
            
        except Exception as e:
            print("Error ", e)
    async def pingall(self, ctx):
        messageembed = discord.Embed(
                                title="PEACE TIME OVER!",
                                description="Peace is over :gun:",
                                color=discord.Colour.random()
                            )
        messageembed.set_author(
                                name=botname,
                                icon_url=icon
                            )
        messageembed.set_footer(text="Goodluck")
        allowed_mentions = discord.AllowedMentions(everyone = True)
        await ctx.send(content = "@everyone", allowed_mentions = allowed_mentions)
        await ctx.send(embed=messageembed)
        return
    async def countdown(self, ctx, message):
        try:
            if self.countdown_time > 3600:
                hours = self.countdown_time // 3600
                editor = await ctx.send(f"In hours: about {hours} hours")
            first_time = True
            while self.countdown_time > 0:
                minutes, seconds = divmod(self.countdown_time, 60)
                hours, minutes = divmod(minutes, 60)
                if first_time:
                    await message.edit(content = f"Countdown has started. Counting down from {hours}h {minutes}m and {seconds}s.")
                    first_time = False
                if self.countdown_time > 3600:
                    # Update editor message with remaining hours
                    await editor.edit(content=f"In hours: about {hours} hours")
                
                await message.edit(content=f"Countdown: {hours}h {minutes}m {seconds}s (will iterate every 60 seconds)")
                
                await asyncio.sleep(60)
                self.countdown_time -= 60
            
            await message.edit(content="Countdown finished!")
            await self.pingall(ctx)
            await self.peacetimereset(ctx, self.startingseconds)
            self.warmode = True  
        except asyncio.CancelledError:
            # This exception will be raised when the countdown is cancelled
            pass
        except Exception as e:
            print("Error ", e)
    @commands.command()
    async def checkwarmode(self, ctx):
        await ctx.send(f"IS warmode active: {self.warmode}")
   
    async def peacetime_resend(self, ctx):
            messageembed = discord.Embed(
                                    title="Peace time is active again!",
                                    description="Peace is active :peace:",
                                    color=discord.Colour.random()
                                )
            messageembed.set_author(
                                    name=botname,
                                    icon_url=icon
                                )
            messageembed.set_footer(text="Finally..")
            allowed_mentions = discord.AllowedMentions(everyone = True)
            await ctx.send(content = "@everyone", allowed_mentions = allowed_mentions)
            await ctx.send(embed=messageembed)
            return

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def peacetimereset(self, ctx, seconds: int):
        try:
            self.resettime = seconds
            remaining_seconds = seconds
            message = await ctx.send(f"Countdown started for {self.countdown_time} seconds!")
            if seconds <= 0:
                await ctx.send("Input a positive number to start the countdown.")
            if seconds < 60:
                await ctx.send("Can't choose a number less than 60!") 
                return
                

            self.resettime_task = asyncio.create_task(self.peacetimeresetcountdown(ctx, message, remaining_seconds))

        except Exception as e:
            print("Error, ", e)
            traceback.print_exc()

    async def peacetimeresetcountdown(self, ctx, message, remaining_seconds):
            try:
                if remaining_seconds > 3600:
                    hours = remaining_seconds // 3600
                    editor = await ctx.send(f"In hours: about {hours} hours")
                first_time = True
                while self.resettime > 0:
                    minutes, seconds = divmod(self.resettime, 60)
                    hours, minutes = divmod(minutes, 60)
                    if first_time:
                        await message.edit(content = f"Countdown has started. Counting down from {hours}h {minutes}m and {seconds}s.")
                        first_time = False
                    if self.resettime > 3600:
                        await editor.edit(content=f"In hours: about {hours} hours")
                    await message.edit(content=f"WarTime Countdown(if running means warmode is active): {hours}h {minutes}m {seconds}s (will iterate every 60 seconds)")

                    await asyncio.sleep(60)
                    self.resettime -= 60
                await message.edit(content="Countdown finished!")
                await self.peacetime_resend(ctx)
                await self.settimer(ctx, remaining_seconds)
            except Exception as e:
                print("Error", e)
                traceback.print_exc()

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def declarewaroverrule(self, ctx, member: str , user: discord.Role = None):
            if self.warmode == True:
                if "@" in member:
                    try:
                        await ctx.send(f"A war declaration has been overruled and made on one of the clans! User {member} has declared war on {user.mention}")
                    except Exception:
                        traceback.print_exc()
                        await ctx.send("Mention a real clan role.")
                    allowed_mentions = discord.AllowedMentions(everyone = True)
                    await ctx.send(content = "@everyone", allowed_mentions = allowed_mentions)
                else:
                    await ctx.send("Mention a clan to go to war with them!")
            else:
                await ctx.send("Warmode is not active!")

    @commands.command()
    async def declarewar(self, ctx, member: str):
        if self.warmode == True:
            if "@" in member:
                await ctx.send(f"A war declaration has been made on one of the clans! User {ctx.author.mention} has declared war on {member}")
                allowed_mentions = discord.AllowedMentions(everyone = True)
                await ctx.send(content = "@everyone", allowed_mentions = allowed_mentions)
            else:
                await ctx.send("Mention a clan to go to war with them!")
        else:
            await ctx.send("Warmode is not active!")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def warmodeactive(self, ctx):
        self.warmode = True
        await ctx.send(f"Command success. Warmode set to {self.warmode}")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def warmodeoff(self,ctx):
        self.warmode = False
        await ctx.send(f"Command success. Warmode set to {self.warmode}")

    @commands.has_permissions(moderate_members=True)
    @commands.command()
    async def aborttimer(self, ctx):
        try:
            if self.resettime_task is not None and not self.resettime_task.done():
                self.resettime_task.cancel()
                self.resettime_task = None
                self.resettime = None
            if self.countdown_task is not None and not self.countdown_task.done():
                self.countdown_task.cancel()
                self.countdown_task = None
                self.countdown_time = None
                await ctx.send("Countdown has been aborted.")
            else:
                await ctx.send("Aborted.")
        except Exception as e:
            print("Error ", e)

    @commands.command()
    async def peacetime(self, ctx):
        try:
            messageembed = discord.Embed(
                        title="Peacetime :peace:",
                        description=f"There is {self.countdown_time} seconds of peace time left.",
                        color=discord.Colour.random()
                    )
            messageembed.set_author(
                        name=botname,
                        icon_url=icon
                    )
            messageembed.set_footer(text="Get ready!")
            if self.countdown_time == None:
                await ctx.send("There is no peacetime timer running!")
                return      
            elif self.warmode is True:
                await ctx.send("Warmode is active, peace time is off!") 
            else:
                await ctx.send(embed=messageembed)
            
            
        except TypeError:
            pass
        except Exception as e:
            print("Error", e)

    @commands.command()
    async def wartime(self, ctx):
        try:
            messageembed = discord.Embed(
                        title="WARTIME :gun:",
                        description=f"There is {self.resettime} seconds of war time left.",
                        color=discord.Colour.random()
                    )
            messageembed.set_author(
                        name=botname,
                        icon_url=icon
                    )
            messageembed.set_footer(text="dont stop the killing!")
            if self.resettime is None:
                await ctx.send("There is no war timer running!")
                return       
            elif self.warmode == False:
                messageembed = discord.Embed(
                        title="WAR is off :gun:",
                        description=f"Warmode is currently off.",
                        color=discord.Colour.random()
                    )
                messageembed.set_author(
                        name=botname,
                        icon_url=icon
                    )
                messageembed.set_footer(text="phew")
                await ctx.send(embed=messageembed)
            else:
                await ctx.send(embed=messageembed)
            

        except TypeError:
            pass
        except Exception as e:
            print("Error", e)

    
async def setup(bot):
    await bot.add_cog(PeaceTimer(bot))