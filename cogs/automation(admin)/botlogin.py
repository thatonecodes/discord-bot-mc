import discord
from discord.ext import commands
from pyppeteer import launch, browser, page
from pyppeteer.errors import ElementHandleError
import io
import os
import re
from config import consolelink, loginUSERNAME, loginPASSWORD
import asyncio
import traceback


class BotLogin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.countdown_embed = None
        self.botloggedin = False
    async def initialize_driver(self):
        self.driver = await launch()
        self.Newpage = await self.driver.newPage()

    @commands.has_permissions(administrator = True)
    @commands.command()
    async def botlogin(self, ctx):
        try:
            while True:
                await self.initialize_driver()    
                newpage = self.Newpage     
                await newpage.goto(consolelink)
                try:
                    name = await newpage.querySelector("#LoginForm_name")
                    if name:
                        message = await ctx.send("Loading...")
                        await asyncio.sleep(5)
                        await name.type(loginUSERNAME)
                        await message.edit(content="usrname PASS")
                        await asyncio.sleep(5)
                        await message.edit(content="entr")
                        await asyncio.sleep(5)
                        
                        password = await newpage.querySelector("#LoginForm_password")
                        if password:
                            
                            savebtn = await newpage.querySelector("#LoginForm_rememberMe")
                            if savebtn:
                                await savebtn.click()
                                await message.edit(content="password PASS")
                                await password.type(loginPASSWORD)
                                await password.press("Enter")
                                await newpage.waitForNavigation()
                                await newpage.screenshot({'path': 'example.png'})
                                await message.edit(content="Checking for usr block..")
                                try:
                                    form = await newpage.querySelector(".form")
                                    if form is None:
                                        await message.edit(content="successful login!")
                                        self.botloggedin = True
                                        break
                                    else:
                                        print("form error")
                                        raise Exception
                                except Exception as e:
                                    print("Error :", e)
                                    traceback.print_exc()
                                
                                
                            else:
                                await message.edit(content="Save button not found.")
                        else:
                            await message.edit(content="Password input field not found.")
                    else:
                        await message.edit(content="Name input field not found.")
                    
                    
                        
                        
                except Exception as e:
                    print(e)
                    traceback.print_exc()
                    await ctx.send("An error occured.")
                    break
                    
                        
                else:
                    error = await newpage.querySelector(".errorMessage")
                    if error is None:
                        pass
                    elif error is not None:
                        errortext = await newpage.evaluate('(element) => element.textContent', error)
                        await message.edit(content = f"Unsuccessful login.. {errortext} trying to await for 30 seconds..")
                        await asyncio.sleep(30)
                        continue
                
                    
            
        except Exception as e:
            print("ERROR EXECPTION ", e, traceback.print_exc())


    @commands.has_permissions(administrator = True)
    @commands.command()     
    async def announce(self, ctx, *, annoucement: str):
        try:
            page = self.Newpage
            if self.botloggedin is True:
                consolearea = await page.querySelector("#command")
                await consolearea.type(f"/say {annoucement}")
                await consolearea.press("Enter")
                await ctx.send("Sent announcement!")
                return
            if self.botloggedin != True:
                await ctx.send("Cannot run this command without $botlogin!")
                return
            else:
                await ctx.send("An error occured.")
                traceback.print_exc()
                return
        except AttributeError:
            await ctx.send("Cannot run this command without $botlogin!")
            return
        except Exception as e:
            print("error, exepction", e)
            traceback.print_exc()

    
    @commands.has_permissions(administrator = True)
    @commands.command()             
    async def consolecommand(self, ctx, *, command: str):
        try:
            page = self.Newpage
            if self.botloggedin is True:
                consolearea = await page.querySelector("#command")
                await consolearea.type(f"{command}")
                await consolearea.press("Enter")
                await ctx.send("Sent command to console!")
            if self.botloggedin != True:
                await ctx.send("Cannot run this command without $botlogin!")
                return
        except Exception as e:
            print("ERROR Excecptions ", e)

    @commands.has_permissions(administrator = True)
    @commands.command() 
    async def console(self, ctx):
        try:
            page = self.Newpage
            if self.botloggedin is True:
                consoleareaprev = await page.querySelector(".logArea")
                text_content = await page.evaluate('(element) => element.textContent', consoleareaprev)
                prevfile = io.BytesIO(text_content.encode())
                temporarylocation="console.txt"
                with open(temporarylocation, 'wb') as out: 
                    out.write(prevfile.getbuffer())
                    # Search with regex to find matches of email
                    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    pattern = r"\d{2}\.\d{2} \d{2}:\d{2}:\d{2} \[[^\]]+\]"
                    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
                    coordpattern = r'x=[+-]?\d+(\.\d+)?, y=[+-]?\d+(\.\d+)?, z=[+-]?\d+(\.\d+)?'
                    
                        # Remove emails from the console log    
                    new_text = re.sub(pattern, r"\n\g<0>", prevfile.getvalue().decode())
                    clean_console = re.sub(email_pattern, 'Server', new_text)
                    clean_console = re.sub(ip_pattern, 'REMOVED', clean_console)
                    clean_console = re.sub(coordpattern, '[redacted]', clean_console)
                        
                    with open(temporarylocation, 'w') as out:
                        out.write(clean_console)
                        
                    await ctx.send(f"All emails successfuly removed from console log. (Removed)")
                        
                    await ctx.send(f"User Identifiers Successfuly removed from console log. (Removed)")
                
                    
                    await ctx.send(file=discord.File(temporarylocation))
                    os.remove(temporarylocation) 
                
                await ctx.send("finished")
            elif self.botloggedin != True:
                await ctx.send("Cannot run this command without $botlogin!")
                return
                

        except Exception as e:
            print("ERROR Excecptions ", e)

    @commands.has_permissions(administrator = True)
    @commands.command() 
    async def serveron(self, ctx):
        try:
            page = self.Newpage
            if self.botloggedin is True:
                startbutton = await page.querySelector("#yt0")
                is_disabled = await page.evaluate('(element) => element.hasAttribute("disabled")', startbutton)
                if not is_disabled:
                    await startbutton.click()
                    clickembed = discord.Embed(
                    title="Server starting..",
                    description="Server will be up shortly",
                    color=discord.Colour.random()
                    )
                    await ctx.send(embed=clickembed)
                else:
                    await ctx.send("You cannot start a server that is already running!")
                    return
            elif self.botloggedin != True:
                await ctx.send("Cannot run this command without $botlogin!")
                return
        except Exception as e:
            print("EXECPTIONS ", e)
    @commands.has_permissions(administrator = True)
    @commands.command() 
    async def serveroff(self, ctx):
        try:
            page = self.Newpage
            if self.botloggedin is True:
                offbtn = await page.querySelector("#yt1")
                is_disabled = await page.evaluate('(element) => element.hasAttribute("disabled")', offbtn)
                if not is_disabled:
                    await offbtn.click()
                    offbtnr = discord.Embed(
                    title="Server Stopping :Stop:..",
                    description="Server will be stopped shortly",
                    color=discord.Colour.random()
                    )
                    await ctx.send(embed=offbtnr)
                else:
                    await ctx.send("You cannot stop a server that is already stopped!")
                    return
            elif self.botloggedin != True:
                await ctx.send("Cannot run this command without $botlogin!")
                return
        except Exception as e:
            print("EXECPTIONS ", e)

    @commands.has_permissions(administrator = True)
    @commands.command() 
    async def serverrestart(self, ctx):
        try:
            page = self.Newpage
            if self.botloggedin is True:
                restartbtn = await page.querySelector("#yt2")
                is_disabled = await page.evaluate('(element) => element.hasAttribute("disabled")', restartbtn)
                if not is_disabled:
                    await restartbtn.click()
                    restartembed = discord.Embed(
                    title="Server Restarting ..",
                    description="Server will restart shortly",
                    color=discord.Colour.random()
                    )
                    await ctx.send(embed=restartembed)
                else:
                    await ctx.send("You cannot stop a server that is already stopped!")
                    return
            elif self.botloggedin != True:
                await ctx.send("Cannot run this command without $botlogin!")
                return
        except Exception as e:
            print("EXECPTIONS ", e)

    @commands.has_permissions(administrator = True)
    @commands.command() 
    async def botexit(self, ctx):
        try:
            if self.botloggedin is True:
                exitembed = discord.Embed(
                    title="Exiting driver..",
                    description="Exiting in a moment.",
                    color=discord.Colour.random()
                )
                await ctx.send(embed=exitembed)
                self.botloggedin = False
                await self.driver.close()
                await ctx.send("Exit success.")
            elif self.botloggedin != True:
                await ctx.send("Cannot exit non running driver!")
        except Exception as e:
            print("Errno ", e)
    
    @commands.has_permissions(administrator = True)
    @commands.command() 
    async def botrestart(self,ctx):
        try:
            if self.botloggedin is not True:
                await self.botlogin(ctx)
                self.botloggedin = True
                await ctx.send("Bot has restarted.")
            elif self.botloggedin == True:
                await ctx.send("Restarting prerunning bot.")   
                await self.botlogin(ctx)
                self.botloggedin = True
        except Exception as e:
            print(e)
         
            
async def setup(bot):
    await bot.add_cog(BotLogin(bot))