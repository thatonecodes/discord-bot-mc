import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import io
import os
import re
from config import consolelink, loginUSERNAME, loginPASSWORD
import asyncio

class BotLogin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.options = webdriver.ChromeOptions()
        self.botloggedin = False
        self.countdown_embed = None

    def initialize_driver(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(options=options)

    @commands.has_permissions(administrator = True)
    @commands.command()
    async def botlogin(self, ctx):
        try:
            while True:
                self.initialize_driver()         
                self.driver.get(consolelink)
                name = self.driver.find_element(By.ID, "LoginForm_name")
                message = await ctx.send("Loading...")
                await asyncio.sleep(5)
                name.send_keys(loginUSERNAME)
                await message.edit(content = "usrname PASS")
                await asyncio.sleep(5)
                name.send_keys(Keys.ENTER)
                await message.edit(content = "entr")
                await asyncio.sleep(5)
                password = self.driver.find_element(By.ID, "LoginForm_password")
                password.send_keys(loginPASSWORD)
                savebtn = self.driver.find_element(By.ID, "LoginForm_rememberMe")
                savebtn.click()
                await message.edit(content = "password PASS")
                await asyncio.sleep(5)
                password.send_keys(Keys.ENTER)
                self.driver.get_screenshot_as_file("screenshot.png")
                await message.edit(content = "Checking for usr block..")
            
                
                try:
                    error = self.driver.find_element(By.CLASS_NAME, "errorMessage")
                except NoSuchElementException:
                    await message.edit(content = "Login Successful!")
                    self.botloggedin = True
                    break
                    
                else:
                    await message.edit(content = f"Unsuccessful login.. {error.text} trying to await for 30 seconds..")
                    await asyncio.sleep(30)
                    continue
                
                    
            
        except Exception as e:
            print("ERROR EXECPTION ", e)

    @commands.has_permissions(administrator = True)
    @commands.command()     
    async def announce(self, ctx, annoucement: str):
        try:
            if self.botloggedin is True:
                consolearea = self.driver.find_element(By.ID, "command")
                consolearea.send_keys(f"/say {annoucement}")
                consolearea.send_keys(Keys.ENTER)
                await ctx.send("Sent announcement!")
            elif self.botloggedin != True:
                await ctx.send("Cannot run this command without $botlogin!")
                return
        except Exception as e:
            print("error, exepction", e)

    @commands.has_permissions(administrator = True)
    @commands.command()             
    async def consolecommand(self, ctx, command: str):
        try:
            if self.botloggedin is True:
                consolearea = self.driver.find_element(By.ID, "command")
                consolearea.send_keys(f"{command}")
                consolearea.send_keys(Keys.ENTER)
                await ctx.send("Sent command to console!")
            elif self.botloggedin != True:
                await ctx.send("Cannot run this command without $botlogin!")
                return
        except Exception as e:
            print("ERROR Excecptions ", e)
            
    @commands.has_permissions(administrator = True)
    @commands.command() 
    async def console(self, ctx):
        try:
            if self.botloggedin is True:
                consoleareaprev = self.driver.find_element(By.CLASS_NAME, "logArea")
                prevfile = io.BytesIO(consoleareaprev.text.encode())
                temporarylocation="console.txt"
                with open(temporarylocation, 'wb') as out: 
                    out.write(prevfile.getbuffer())
                    # Search with regex to find matches of email
                    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    emails_found = re.findall(email_pattern, prevfile.getvalue().decode())
                    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
                    ips_found = re.findall(ip_pattern, prevfile.getvalue().decode())
                    if emails_found:
                        # Remove emails from the console log
                        clean_console = re.sub(email_pattern, 'Server', prevfile.getvalue().decode())
                        with open(temporarylocation, 'w') as out:
                            out.write(clean_console)
                        
                        await ctx.send(f"All emails successfuly removed from console log. (Removed)")
                    else:
                        pass
                    if ips_found:
                        clean_console = re.sub(ip_pattern, '', prevfile.getvalue().decode())
                        with open(temporarylocation, 'w') as out:
                            out.write(clean_console)
                        
                        await ctx.send(f"User Identifiers Successfuly removed from console log. (Removed)")
                    else:
                        pass
                
                    
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
            if self.botloggedin is True:
                startbutton = self.driver.find_element(By.ID, "yt0")
                if startbutton.get_attribute("disabled") is None:
                    startbutton.click()
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
            if self.botloggedin is True:
                offbtn = self.driver.find_element(By.ID, "yt1")
                if offbtn.get_attribute("disabled") is None:
                    offbtn.click()
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
            if self.botloggedin is True:
                restartbtn = self.driver.find_element(By.ID, "yt2")
                if restartbtn.get_attribute("disabled") is None:
                    restartbtn.click()
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
                self.driver.quit()
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
                self.botlogin()
                self.botloggedin = True
                await ctx.send("Bot has restarted.")
            elif self.botloggedin == True:
                await ctx.send("Bot is already running! You need to $botexit it to run this command!")   
        except Exception as e:
            print(e)
         
            
async def setup(bot):
    await bot.add_cog(BotLogin(bot))