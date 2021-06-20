#
#
#
#
#
import discord
from discord import utils
import re
import os
from discord.ext import commands
import youtube_dl
from queries import *

coin = [':disguised_face:', ':peach:']

special_user = 417772375199711242

client = commands.Bot(command_prefix='.', intents = discord.Intents.all())

#bot ready confirmation
@client.event
async def on_ready():
    print(f'logged on as {client.user}!')

# @client.event
# async def on_voice_state_update(member, before, after):
#   # voice = member.guild.voice_client

#   if before.channel is None and after.channel is not None:
#       voiceChannel = await after.channel.connect()
      
#       if os.getcwd() != os.getenv('main_path') + '/John Cena':
#           os.chdir(str(os.getenv('main_path') + '/John Cena'))
#       for file in os.listdir(os.getcwd()):
#           if file.endswith('.mp3'):
#               voiceChannel.play(discord.FFmpegPCMAudio(file))
#       while voiceChannel.is_playing():
#           pass
#       if voiceChannel.is_connected():
#           await voiceChannel.disconnect()
#       os.chdir(os.getenv('main_path'))


@client.command(hidden=True)
async def load(extension):
    client.load_extension(f'cogs.{extension}')

@client.command(hidden=True)
async def unload(extension):
    client.unload_extension(f'cogs.{extension}')

@client.command(hidden=True)
async def reload(ctx):
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            try:
                client.unload_extension(f'cogs.{file[:-3]}')
                client.load_extension(f'cogs.{file[:-3]}')
            except:
                await ctx.send(f'An error occured... a {file} not reloaded...')
    await ctx.send('Cogs reloaded')
        


for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))

