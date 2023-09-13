import disnake as discord
from disnake.ext import commands
import os
from decouple import config

# Define the intents for the bot
intents = discord.Intents.all()

# Create a bot instance with the specified command prefix and intents
bot = commands.Bot(command_prefix="H!", intents=intents)


# Event handler: This block of code executes when the bot is ready
@bot.event
async def on_ready():
    # await bot.change_presence(status=discord.Status.idle)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="techcafe.ir"))
    print(f'We have logged in as {bot.user}')

    # Load cogs from the 'cogs' directory
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'\033[32m"{filename[:-3]}" cog loaded')
            except Exception as e:
                print(f'\033[31mFailed to load "{filename[:-3]}" detail: [{e}]')


# Slash command: A simple ping command to check bot latency
@bot.slash_command(name="ping", description="get bot ping")
async def ping(inter):
    await inter.response.send_message(f"**Bot ping : {round(bot.latency * 1000)}ms**", ephemeral=True)

# Event handler: This block of code handles errors that occur during command execution
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        pass

# Run the bot with the provided token from environment variables
bot.run(config("BOT_TOKEN", default="test"), reconnect=True)
