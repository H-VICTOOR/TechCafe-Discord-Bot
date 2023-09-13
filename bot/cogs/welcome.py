import disnake as discord
from disnake.ext import commands


# Create a Welcome cog for handling new member joining events
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channel_id = 1052601454914981920 # Set the ID of the welcome channel


    # Listener for the 'on_member_join' event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Get the welcome channel using the stored ID
        welcome_channel = self.bot.get_channel(self.welcome_channel_id)
        try:
            # Create an embed for the welcome message
            embed = discord.Embed(
            title=f"Welcome to {member.guild.name}",
            description="We're glad you're here.",
            color=0xD9D9D9
        )
            # Set the member's avatar as the thumbnail
            embed.set_thumbnail(url=member.avatar)
            # Add fields for username and ID
            embed.add_field(name="Username", value=member.name, inline=True)
            embed.add_field(name="ID", value=member.id, inline=True)
            # Set the footer text
            embed.set_footer(text="Developed By H_VICTOR")

            await welcome_channel.send(embed=embed)
        except Exception as e:
            print(e) # Print the error for debugging
            pass # Continue execution even if an error occurs

# Function to add the Welcome cog to the bot
def setup(bot):
    bot.add_cog(Welcome(bot))
