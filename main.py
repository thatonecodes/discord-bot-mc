import discord
import config
from discord.ext import commands
from PIL import Image
import io
import traceback
import random
import requests
from bs4 import BeautifulSoup
import datetime
import base64
import os


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}")
    print("Login successful!")


#bot propeties
icon = "https://i.ytimg.com/vi/ihCsolHId7A/maxresdefault.jpg"
botname = "Minecraft Chad"


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        notfound = discord.Embed(
            title="Command not found!",
            description="Invalid command. Use $help to see all available commands.",
            color=discord.Color.red()
        )
        notfound.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        await ctx.send(embed=notfound)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes: (ex. $ban @user trolling)!')
        
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have the perms to run this command :angry:")
@bot.event
async def on_error(ctx, error):
    if isinstance(error, commands.errors.__all__):
        errorEmbed = discord.Embed(
            title="Error!",
            description="An client-side exeception occured!",
            color=discord.Color.red()
        )
        errorEmbed.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        traceback.print_exception()
@bot.command(help="This is the help command, it shows all the commands.")
async def help(ctx):
    all_commands = bot.commands
    command_list = ([f"{command.name}: {command.help}" for command in all_commands])
    unpacked = "\n".join(command_list)

    helpcmds = discord.Embed(
        title=f"Help & all commands!",
        description=f"The commands are ($): \n{unpacked}",
        color=discord.Colour.random()
    )
    helpcmds.add_field(name="Usage", value="To use the bot, simply put a $ in front of the command. (ex $help, $rules)", inline= False)
    helpcmds.set_author(
        name=f"{botname}",
        icon_url=f"{icon}"
    )
    helpcmds.set_footer(text="created by dionednrg")
    await ctx.send(embed=helpcmds)
@bot.command(help="Shows rules for the server.")
async def rules(ctx):
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

#jojo
@bot.command(help="makes you dio (KONO DIO DA!)")
async def konodioda(ctx, member: discord.Member = None):
    try:
        member = member or ctx.author  # If no member is provided, use the author of the command
        # Fetch the user's avatar as bytes
        avatar_bytes = await member.avatar.read()

        # Open the background image on which you want to put the avatar
        background_image = Image.open("background_image.png")

        # Open the avatar image from the bytes
        avatar_image = Image.open(io.BytesIO(avatar_bytes))

        # Resize the avatar to fit your desired position
        avatar_size = (390, 390)
        avatar_image = avatar_image.resize(avatar_size)

        # Position the avatar on the background image
        position = (470, 50)
        background_image.paste(avatar_image, position)

        # Save the final image with the avatar
        final_image_path = "background_image_modified.png"
        background_image.save(final_image_path)

        # Send the final image in the Discord channel
        with open(final_image_path, "rb") as f:
            await ctx.send(file=discord.File(f))

        # Clean up temporary image files (optional)
        background_image.close()
        avatar_image.close()
    except Exception as e:
        errorEmbed = discord.Embed(
            title="Error!",
            description="An error occured!",
            color=discord.Color.red()
        )
        errorEmbed.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        await ctx.send(embed=errorEmbed)
        traceback.print_exception()

@bot.command(help="you get to finger someone :point_right:")
async def star_finger(ctx, member: discord.Member = None):
    try:
        if member == None:
            await ctx.send("Choose a member($star_finger @user)!")
            return
        member = member
        
        finger = discord.Embed(
            title="GAH DAM - :point_right:",
            description=f"{ctx.author.mention} fingers {member.mention}!",
            color=discord.Colour.random()
        )

        urls = ["https://media.tenor.com/SqcvxN7Pfl0AAAAC/star-platinum.gif", "https://media.tenor.com/0m6Po4t45AoAAAAd/polnareff-polnareff-star-finger.gif", "https://media.tenor.com/RwQPqlGzyBcAAAAC/star-platinum-jojo.gif"]
        finger.set_image(url= random.choice(urls))


        await ctx.send(embed=finger)
    except Exception as e:
        traceback.print_exc()
        

@bot.command(help="Get a stand! (JOJO)")
async def stand(ctx):
    try:
        loading_msg = await ctx.send("Parsing stands, please wait...")
        url = "https://jojowiki.com/List_of_Stands"
        get_url =  requests.get(url)
        soup = BeautifulSoup(get_url.content, "html.parser")
        all_stands = []
        all_links = []
        formatted_links = []
        stands = soup.find_all("div", class_="charbox")
        for stand in stands:
            char_img = stand.find("img")["src"].strip()
            char_src = stand.find("a")["href"].strip()
            char_name = stand.find("div", class_="charname").text.strip()
            char_stand = stand.find("div", class_="charstand").text.strip()
            all_stands.append((char_name, char_stand))
            all_links.append((char_img,char_src))
    
        for img, src in all_links:
            if "%27" in src:
                formatted_src1 = src.replace("%27", "'").replace("_", " ")
                formatted_src = formatted_src1.lstrip('/').replace('_', ' ')
            elif "%C3%" in src:
                formatted_src1 = src.replace("%C3%", "'").replace("_", " ")
                formatted_src = formatted_src1.lstrip('/').replace('_', ' ')
            elif "%26" in src:
                formatted_src1 = src.replace("%26", "&").replace("_", " ")
                formatted_src = formatted_src1.lstrip('/').replace('_', ' ')
            else:
                formatted_src = src.lstrip('/').replace('_', ' ')
            formatted_links.append((formatted_src, img))

        random_stand_data = []
        random_stand = random.choice(all_stands)
        linker = random_stand[0].replace(" ", "_")
        src = f"https://jojowiki.com/{linker}"
        for formatted_src, img in formatted_links:
            if random_stand[0] == formatted_src:
                random_stand_data.append((random_stand[0], random_stand[1], img, src))
                print("success")
                break
        else:
            await loading_msg.edit(content="No stand found for the given name. Rerun Command!")
            return
        
        
        if len(random_stand_data) > 0:
            name, stand, img, stand_src = random_stand_data[0]
            jojoStand=discord.Embed(
                title=f"Your stand is:\n{name}",
                description=f"{stand}",
                url=f"{stand_src}",
                color=discord.Colour.random()
            )
            jojoStand.set_author(
                name=f"{botname}",
                icon_url=f"{icon}"
            )
            jojoStand.set_image(url=f"{img}")
            jojoStand.set_footer(text="iS tHaT a jOjO rEfErEnCe!1!1!!")
            await ctx.send(embed=jojoStand)
        await loading_msg.edit(content="Stand comparison completed!")
        
    except requests.exceptions.RequestException as e:
        print("Error fetching the URL:", e)
    except Exception as e:
        traceback.print_exc()
        errorEmbed = discord.Embed(
            title="Error!",
            description="An error occured!",
            color=discord.Color.red()
        )
        errorEmbed.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        await ctx.send(embed=errorEmbed)
        
    
        
#minecraft
@bot.command()
async def map(ctx):
    #map is going to be preset image
    pass
@bot.command()
async def find_player(ctx):
    #find player using custom map in server (mod)
    pass
@bot.command(help="Get a minecraft player's skin!")
async def skin(ctx, player):
    try:
        player = player
        if player == None:
            await ctx.send("Please select a player! (ex. $skin [player])")
        url = f"https://minecraftuuid.com/?search={player}"
        get_url = requests.get(url)
        soup = BeautifulSoup(get_url.content, "html.parser")
        input_field = soup.find("input", {"type": "text", "class": "Form-Control", "placeholder": "Trimmed UUID"})
        uuid_value = input_field.get("value")
        skin_image_url = f"https://crafatar.com/renders/body/{uuid_value}"
        name_mc_url = f"https://namemc.com/profile/{player}.1"
        skinEmbed = discord.Embed(
            title=f"Skin of player: {player}",
            description="The player's skin is shown below.",
            color=discord.Colour.random(),
            url= name_mc_url
        )
        skinEmbed.set_image(url=skin_image_url)
        skinEmbed.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        skinEmbed.set_footer( text="* credit to namemc and crafatar for API and links")
        await ctx.send(embed=skinEmbed)

    except AttributeError:
        await ctx.send("Invalid user! Please try again.")
        traceback.print_exc()
    except Exception as e:
        print("execption")
        traceback.print_exc()
        await ctx.send("An error occurred.")

@bot.command()
async def minecraft_server(ctx, ip: str = "Iamthemaster101.aternos.me"):
    #start using the minecraft_server api to interact with servers
    try:
        minecraft_server_url = f"https://api.mcsrvstat.us/2/{ip}"
        response = requests.get(minecraft_server_url)
        data = response.json()

        if "ip" in data and "port" in data:
            ip_address = data["ip"]
            port = data["port"]
            players_online = data["players"]["online"]
            player_info = "No players online"
            max_players = data["players"]["max"]
            version = data["version"]
            is_online = data["online"]
            image_icon = data["icon"]

            base64_data = image_icon.replace("data:image/png;base64,", "")

            # Decode Base64 and create an image from it
            image_data = base64.b64decode(base64_data)
            image = Image.open(io.BytesIO(image_data))

            image_path = "decoded_image.png"
            image.save(image_path)

            if "software" in data:
                software = data["software"]
                
            else:
                software = "Unknown"
            
            information = data["motd"]["clean"]

            minecraft_embed = discord.Embed(
                title=f"Minecraft Server Information for {ip}",
                description=f"""Server IP: {ip_address}:{port}
                Players Online: {players_online}/{max_players}
                Version: {version}
                Online: {is_online}
                Software: {software}
                Description: {' '.join(str(i) for i in information)}""",
                color=discord.Colour.random()
            )
            minecraft_embed.set_author(
                name=botname,
                icon_url=icon
            )
            minecraft_embed.set_footer(text="credit to mcsrvstat for the API")
            with open(image_path, "rb") as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
                await ctx.send(embed=minecraft_embed)
            os.remove(image_path)

    except KeyError:
        traceback.print_exc()
        print("Failed to retrieve server information.")
        await ctx.send("Invalid IP, please try again!")

    except Exception as e:
        traceback.print_exc()
        print("Error occurred while fetching server information.")


#toxic commands
@bot.command(help="LTG says something to you :zap:")
async def ltg(ctx):
    urls = ["https://media.tenor.com/b5uy31YIxE8AAAAd/ltg-low-tier-god.gif", "https://media.tenor.com/2wJ6I1I_tqEAAAAC/ltg-low-tier-god.gif", "https://media.tenor.com/SWRwTE3J_fYAAAAd/ltg.gif", "https://media.tenor.com/JHRBvg3bY68AAAAd/low-tier-god-gtab.gif", "https://media.tenor.com/rtFcrfD0FC8AAAAd/low-tier-god-your-life-has-zero-purpose.gif", "https://media.tenor.com/OGRRT-SrTCIAAAAM/you-should-treat-yourself-now.gif"]
    ltgembed=discord.Embed(
        title="LTG SAYS:",
        description="you should :zap: :zap: :zap: yourself NOW!",
        color=discord.Colour.random()
    )
    ltgembed.set_author(
        name=f"{botname}",
        icon_url=f"{icon}"
    )
    random_url = random.choice(urls)
    ltgembed.set_image(url=random_url)
    if random_url == "https://media.tenor.com/OGRRT-SrTCIAAAAM/you-should-treat-yourself-now.gif":
        ltgembeds=discord.Embed(
        title="LTG SAYS:",
        description="you should :hearts::hearts::hearts: yourself now!",
        color=discord.Colour.random()
    )
        ltgembeds.set_image(url="https://media.tenor.com/OGRRT-SrTCIAAAAM/you-should-treat-yourself-now.gif")

        ltgembeds.set_author(
            name=f"{botname}",
            icon_url=f"{icon}"
        )
        ltgembeds.set_footer(text="thanks!")
        await ctx.send(embed=ltgembeds)
    else:
        ltgembed.set_footer(text="just kidding don't actually do that..(pls)")
        await ctx.send(embed=ltgembed)
    
    
   

@bot.command(help="kill someone(not irl yet) :knife:")
async def kill(ctx, member: discord.Member = None):
    member = member
    if member == None:
        await ctx.send("Select a member!(ex. kill @user)")
        return
    urls = ["https://media.tenor.com/uLq-U2cHgOgAAAAC/point-gun-shoot.gif", "https://i.pinimg.com/originals/04/ef/fa/04effa171ee2ecee7418eb98016d433a.gif", "https://media.tenor.com/u3azQsuPm0QAAAAC/die-gun.gif", "https://media.tenor.com/R9xae2ktRN8AAAAC/bang-deanwinchester.gif", "https://media.tenor.com/Y_inndSQYP8AAAAC/jojo-king-crimson.gif", "https://media.tenor.com/r-mjvq-uBUkAAAAd/gold-experience-requiem-diavolo-jjba.gif"]
    random_url = random.choice(urls)
    killembed=discord.Embed(
        title=":knife: :drop_of_blood: bruh dead",
        description=f"{ctx.author.mention} kills {member.mention}!",
        color=discord.Colour.random()
    )
    killembed.set_image(url=random_url)
    killembed.set_footer(text="just kidding chads never die")
    killembed.set_author(
        name=f"{botname}",
        icon_url=f"{icon}"
    )
    
    
    await ctx.send(embed=killembed)

@bot.command(help="Beat up someone :punch:")
async def beatup(ctx, member: discord.Member = None):
    member = member or ctx.author
    urls = ["https://media.tenor.com/qKTBsktfhSgAAAAd/punch-blue-hoodie.gif", "https://media.tenor.com/DE8TGcQUcMwAAAAC/rapid-punch-twinzero.gif", "https://media.tenor.com/ZXM8sTlvCnQAAAAM/promethozeen.gif", "https://media.tenor.com/LGCkjHzWvecAAAAd/beating-up-beat-up.gif"]
    url_random = random.choice(urls)
    beat_up_embed = discord.Embed(
        title="Fight back, FIGHT BACK!",
        description=f"{ctx.author.mention} beats up {member.mention}",
        color=discord.Colour.random()
    )
    beat_up_embed.set_image(url=url_random)
    beat_up_embed.set_author(
        name=f"{botname}",
        icon_url=f"{icon}"
    )
    beat_up_embed.set_footer( text="he ded :skull:")
    
    await ctx.send(embed=beat_up_embed)

@bot.command(help="cool g u n :gun:")
async def gun(ctx, member: discord.Member = None):
    urls = ["https://media.tenor.com/2p9YmPClM0oAAAAC/justified-gun-spinning.gif", "https://media.tenor.com/AO_oFEKPj4AAAAAC/gun-firing.gif", "https://media.tenor.com/cKFZd3_-4YcAAAAd/call-of-duty-revolver.gif", "https://static.wikia.nocookie.net/valorant/images/2/23/GoldenGun.png/revision/latest?cb=20210122000812", "https://media.tenor.com/opl-nN4yPRwAAAAd/valorant-gun.gif"]
    random_url = random.choice(urls)
    gunEmbed = discord.Embed(
        title="G U N",
        description= ":gun:",
        color=discord.Colour.random()
    )
    gunEmbed.set_author(
        name= botname,
        icon_url= icon
    )
    gunEmbed.set_image(url=random_url)
    await ctx.send(embed=gunEmbed)

#fun commands
@bot.command(help="bruh")
async def bruh(ctx):
    urls = ["https://us-tuna-sounds-images.voicemod.net/8657d656-18f5-470f-8303-c95f4f3fbfd6-1664164407190.jpg", "https://images.genius.com/12719860cb2edd87f3a7abea741a70ba.1000x1000x1.jpg", "https://static.truckersmp.com/images/vtc/logo/21823.1594940844.png", "https://i1.sndcdn.com/avatars-U3ir1j6Qhg3QxaII-zPG37Q-t500x500.jpg"]
    random_url = random.choice(urls)
    bruhEmbed = discord.Embed(
        title="bruh",
        description="bruh moment",
        color= discord.Colour.random()
    )
    bruhEmbed.set_author(
        name= botname,
        icon_url= icon
    )
    bruhEmbed.set_image(url=random_url)
    await ctx.send(embed=bruhEmbed)
@bot.command(help="fuc* someone! (pls no)")
async def fucvk(ctx, member: discord.Member = None):
    try:
        urls = [
            "https://c.tenor.com/FmBSx-Wr1QgAAAAd/anime-redo-of-healer.gif",
            "https://i.pinimg.com/originals/f7/2f/1b/f72f1b87e0036e75dd6bcf2a3a1bb504.gif",
            "https://media.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif",
            "https://media.tenor.com/EW4YboL_nl0AAAAd/dio-brando-the-world.gif"
        ]
        random_url = random.choice(urls)
        if member is None:
            await ctx.send("Select a member ($fucvk @user)!")

        fucvkEmbed = discord.Embed(
            title="Oh my :scream: what are you-",
            description=f"{ctx.author.mention} fuc*s {member.mention}",
            color=discord.Colour.random()
        )
        fucvkEmbed.set_author(
            name=botname,
            icon_url=icon
        )
        fucvkEmbed.set_image(url=random_url)

        if random_url == "https://c.tenor.com/FmBSx-Wr1QgAAAAd/anime-redo-of-healer.gif":
            fucvkEmbed.set_footer(text="this is ptsd")
        elif random_url == "https://media.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif":
            fucvkEmbed.set_author(
                name="NO",
                icon_url=icon
            )
            fucvkEmbed.description = f"GO TO HORNY JAIL {ctx.author.mention}!"
        elif random_url == "https://media.tenor.com/EW4YboL_nl0AAAAd/dio-brando-the-world.gif":
            fucvkEmbed.title = "THE WORLD!"
            fucvkEmbed.description = f"GO TO HORNY JAIL {ctx.author.mention}!"
            fucvkEmbed.set_author(
                name="no more horny",
                icon_url=icon
            )
            fucvkEmbed.set_footer(text="DIO SAMA")
        
        await ctx.send(embed=fucvkEmbed)
    except Exception as e:
        traceback.print_exc()
        
    
@bot.command(help="In love? Kiss someone! :heart:")
async def kiss(ctx, member: discord.Member = None):
    urls = ["https://media.giphy.com/media/l4FsKa1n9fyStiwZW/giphy.gif", "https://c.tenor.com/wDYWzpOTKgQAAAAC/anime-kiss.gif", "https://media.tenor.com/217aKgnf16sAAAAC/kiss.gif", "https://c.tenor.com/el8DHxNp9IsAAAAC/kiss-anime-love.gif"]
    if member == None:
        await ctx.send("Select a user (ex. $kiss @user)!")
    random_url = random.choice(urls)
    kissEmbed = discord.Embed(
        title=":heart: wow!",
        description=f"{ctx.author.mention} kissed {member.mention}",
        color=discord.Colour.random()
    )
    kissEmbed.set_image(url=random_url)
    kissEmbed.set_footer(text="nice")
    kissEmbed.set_author(
        name=f"{botname}",
        icon_url=f"{icon}"
    )
    await ctx.send(embed=kissEmbed)
@bot.command(help="Annoyed at someone? Slap them! :hand_splayed:")
async def slap(ctx, member: discord.Member = None):
    urls = ["https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif", "https://i.gifer.com/XaaW.gif", "https://c.tenor.com/noSQI-GitQMAAAAC/mm-emu-emu.gif", "https://i.imgur.com/fm49srQ.gif", "https://media.tenor.com/zYf61efRHoIAAAAd/slap-contest-hit-hard.gif"]
    random_urls = random.choice(urls)
    if member == None:
        await ctx.send("Select a user (ex $slap @user)!")
    slapembed = discord.Embed(
        title="SLAP!",
        description=f"{ctx.author.mention} slaps {member.mention}!",
        color=discord.Colour.random()
    )
    slapembed.set_author(
        name=f"{botname}",
        icon_url=f"{icon}"
    )
    slapembed.set_footer(text="ouch")
    slapembed.set_image(url=random_urls)
    await ctx.send(embed=slapembed)
@bot.command(help="Bully someone.. (don't try this at home)")
async def bully(ctx, member: discord.Member = None):
    urls = []
    random_urls = random.choice(urls)
    if member == None:
        await ctx.send("Select a user (ex $bully @user)!")
    bullyembed = discord.Embed(
        title="A bully!",
        description=f"{ctx.author.mention} bullies {member.mention}!",
        color=discord.Colour.random()
    )
    bullyembed.set_author(
        name=f"{botname}",
        icon_url=f"{icon}"
    )
    bullyembed.set_footer(text="do not try this at home")
    bullyembed.set_image(url=random_urls)
    await ctx.send(embed=bullyembed)

@bot.command(help="Greet a friend! :wave:")
async def greet(ctx, member: discord.Member = None):
    member = member
    urls = ["https://c.tenor.com/FMpLzF4UJhwAAAAC/kisumi-wave.gif", "https://media.tenor.com/47GM87fDYNYAAAAC/shouko-nishimiya-bow.gif", "https://media.giphy.com/media/AFdcYElkoNAUE/giphy.gif", "https://i.gifer.com/origin/55/55f1f99ec4fceab6af26e290a9bccdcd_w200.gif"]
    random_urls = random.choice(urls)
    
    if member == ctx.author:
        greetEmbed = discord.Embed(
            title="It's okay..",
            description="I feel the same way manye..",
            color=discord.Colour.blue()
        )
        greetEmbed.set_image(url="https://media.tenor.com/6guCYKvjVcAAAAAd/sad-sad-spongebob-gif.gif")
        greetEmbed.set_footer(text="feelsbadman")
    elif member == None:
        await ctx.send("Select a user(ex $greet @user)!")
    else:
        greetEmbed = discord.Embed(
            title="Hi, how are ya?",
            description=f"{ctx.author.mention} greets {member.mention}!",
            color=discord.Colour.random()
        )
        # Select a random URL from the list of URLs
        greetEmbed.set_image(url=random_urls)
        greetEmbed.set_footer(text="wholesome moment")

    greetEmbed.set_author(
        name=botname,
        icon_url=icon
    )
    
    
    await ctx.send(embed=greetEmbed)

@bot.command(help="find out if you are halal")
async def halal(ctx, member: discord.Member = None):
    member = member or ctx.author.mention
    urls = ["https://media.tenor.com/pzIefmS6xs4AAAAM/ayaan-ayaanus.gif", "https://media.tenor.com/L2n8XN3fvQQAAAAd/halal.gif", "https://media.tenor.com/Ma1qzPPhgHkAAAAM/breaking-bad-halal.gif"]
    random_url = random.choice(urls)
    halalEmbed = discord.Embed(
        title="So Halal mode!",
        description=f"{ctx.author.mention} thinks {member.mention} is halal!",
        color=discord.Colour.random()
    )
    halalEmbed.set_author(
        name=botname,
        icon_url=icon
    )
    halalEmbed.set_footer(text="halal")
    halalEmbed.set_image(random_url)

    await ctx.send(embed=halalEmbed)   

@bot.command(help="this is so haram brother :pig:")
async def haram(ctx):
    member = member or ctx.author.mention
    urls = ["https://media.tenor.com/usOrpkZk9QIAAAAM/haram-heisenberg.gif", "https://media.tenor.com/u5XBzG63c7YAAAAC/haram-andrew-tate.gif"]
    random_url = random.choice(urls)
    haramEmbed = discord.Embed(
        title="So NOT HALAL mode!",
        description=f"{ctx.author.mention} thinks {member.mention} is HARAM!",
        color=discord.Colour.random()
    )
    haramEmbed.set_author(
        name=botname,
        icon_url=icon
    )
    haramEmbed.set_footer(text="haram")
    haramEmbed.set_image(random_url)

    await ctx.send(embed=haramEmbed)   

#moderation
@bot.command(help="ban someone! :hammer:")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*, reason = None):
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

@bot.command(help="kick someone! :leg:")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
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

@bot.command(help="Clear lots of messages! (admin cmd)")
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    try:
        if 1 <= amount <= 100:
            deleted = await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"Deleted {len(deleted) - 1} message(s)!")
        else:
            await ctx.send("Please provide a number between 1 and 100.")
    except Exception as e:
        traceback.print_exc()

@bot.command(help="Timeout someone! :clock:")
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, time, reason=None):
    try:
        if member == None:
            await ctx.send("Select a user! (ex. $timeout @user)!") 
            return
        elif member == ctx.message.author:
            await ctx.channel.send("You cannot timeout yourself!")
            return
        if "h" in time:
            time = time.replace("h","")
            print(time)
        if "d" in time:
            time = time.replace("d","")
            print(time)
        
        await member.timeout(datetime.timedelta(hours=int(time)), reason=reason)
        

        await member.timeout(datetime.timedelta(days=int(time)), reason=reason)
        embed = discord.Embed(title="Timed Out!",
                description=f":white_check_mark: {member.name} has been successfully timed out.",
                color=discord.Colour.random()
                )
        if reason is not None:
            embed = discord.Embed(
                title="Timed Out!",
                description=f":white_check_mark: {member.name} has been successfully timed out for the reason: {reason}.",
                color=discord.Colour.random())
        await ctx.send(embed=embed)
    
    except Exception as e:
        traceback.print_exc()

@bot.command(help="Deafen someone! (in VC) :headphones:")
@commands.has_permissions(moderate_members=True)
async def deafen(ctx, member: discord.Member):
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

@bot.command(help="Mute someone! (in VC) :microphone:")
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
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

bot.run(config.TOKEN)
