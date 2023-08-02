from datetime import datetime
from pytz import timezone
import discord
from discord.ext import commands
import asyncio
from config import botname, icon

class PeaceTimer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tz = timezone('EST')
        self.time = datetime.now(self.tz) 
        self.countdown_time = 0
        self.countdown_task = None

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def countdowntimerset(self, ctx, seconds: str):
        try:
            if seconds == "1d".lower():
                seconds = 86400
            if seconds == "2d".lower():
                seconds = 86400 * 2
            if int(seconds) <= 0:
                await ctx.send("Please enter a positive number for the countdown.")
                return
            
            self.countdown_time = int(seconds)
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
            for i in range(self.countdown_time, 0, -1):
                self.countdown_time = i
                await asyncio.sleep(1)
                if self.countdown_time > 3600:
                    hours = self.countdown_time // 3600
                    hours_remaining = self.countdown_time // 3600
                    await editor.edit(content=f"Hours: {hours_remaining}")
                await message.edit(content=f"Countdown: {i} seconds!")
              
            await message.edit(content="Countdown finished!")
            await self.pingall(ctx)  
        except asyncio.CancelledError:
            # This exception will be raised when the countdown is cancelled
            pass
        except Exception as e:
            print("Error ", e)

    @commands.has_permissions(moderate_members=True)
    @commands.command()
    async def aborttimer(self, ctx):
        try:
            if self.countdown_task is not None and not self.countdown_task.done():
                self.countdown_task.cancel()
                self.countdown_task = None
                self.countdown_time = None
                await ctx.send("Countdown has been aborted.")
            else:
                await ctx.send("There is no ongoing countdown to abort.")
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
            else:
                await ctx.send(embed=messageembed)
            
            while self.countdown_time > 0:
                    
                    await asyncio.sleep(1)
            if self.countdown_time != 0:
                await ctx.send("Peace time is now active!")
        except TypeError:
            pass
        except Exception as e:
            print("Error", e)

    
async def setup(bot):
    await bot.add_cog(PeaceTimer(bot))