import discord
from discord.ext import commands
from PIL import Image
import io
import traceback
from config import icon, botname
import os

class Dio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def konodioda(self, ctx, member: discord.Member = None):
        try:
            member = member or ctx.author  # If no member is provided, use the author of the command
            # Fetch the user's avatar as bytes
            avatar_bytes = await member.avatar.read()

            # Open the background image on which you want to put the avatar
            background_image = Image.open("images/background_image.png")

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
            os.remove(final_image_path)

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

async def setup(bot):
    await bot.add_cog(Dio(bot))
