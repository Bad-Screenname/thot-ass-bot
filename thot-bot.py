import discord
from discord.ext import commands
from discord import utils
import os

client = commands.Bot(command_prefix = '?', intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f'logged in as {client.user}!')

client.run(os.getenv('DISCORD_TOKEN'))
