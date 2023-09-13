import disnake as discord
from disnake.ext import commands
from datetime import datetime

developer_id = [440552369864966144]

# Create a Cog (extension) for text editing commands
class TextEditor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name="say", description="Sends a message to the channel.",)
    async def say(interaction, image: discord.Attachment = None, text: str = None, channel: discord.TextChannel = None,):
        
        channel = channel or interaction.channel
        if image :
            await channel.send(image)
        elif text :
            await channel.send(text)
        else : 
            await interaction.send("You must send one of the fields", ephemeral=True)



    # Define a slash command 'announce' for sending formatted announcements
    @commands.slash_command(name="announce", description="Send a Message")
    async def announce(
        inter,
        content: str = None,
        title: str = None,
        description: str = None,
        color: str = None,
        thumbnail: discord.Attachment = None,
        image: discord.Attachment = None,
        timestamp: bool = False,
        link1: str = None,
        link2: str = None,
        link3: str = None,
        link4: str = None,
        link5: str = None,
        channel: discord.TextChannel = None,
    ):
        # Defer the initial response and indicate that the interaction is ephemeral (only visible to the user)
        await inter.response.defer(with_message=True , ephemeral=True)

        # Process the color input to create a valid discord.Color object
        hex_color = color or '2f3136'
        hex_color = f"#{hex_color}"
        int_color = int(hex_color[1:], 16)


        # Process the links and create discord.ui.Button objects for valid links
        links = [link1, link2, link3, link4, link5]
        buttons = []
        for link in links:
            if link:
                link_parts = link.split('---')
                if len(link_parts) == 2:
                    button_name, button_link = link_parts
                    button = discord.ui.Button(style=discord.ButtonStyle.link, label=button_name, url=button_link)
                    buttons.append(button)

        # Create an ActionRow with buttons if buttons are present, else set to None
        if buttons:
            row = discord.ui.ActionRow(*buttons)
        else:
            row = None

        # Create a list to hold embeds (formatted message)
        embeds = []

        # Create an embed if title or description is provided
        if title or description : # or thumbnail or image
            embed = discord.Embed(color=discord.Color(int_color))

            if title:
                embed.title = title
            if description:
                embed.description = description.replace('{enter}', '\n')

            if thumbnail:
                embed.set_thumbnail(url=thumbnail)

            if image:
                embed.set_image(url=image)

            if timestamp:
                embed.timestamp = datetime.utcnow()


            embeds.append(embed)

        
        # Get the target channel for sending the message, default to the interaction's channel
        channel = channel or inter.channel

        # Trigger typing in the channel
        await channel.trigger_typing()

        # Send the message with provided content, embed, and buttons
        message = await channel.send(
            content=content,
            embed=embeds[0] if embeds else None,
            components=[row] if row else None,
        )
        await inter.edit_original_message("sended")

# Function to add the TextEditor cog to the bot
def setup(bot):
    bot.add_cog(TextEditor(bot))
