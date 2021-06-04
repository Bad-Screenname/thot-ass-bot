#
#
#
#
#
import discord
from discord import utils
import random
import re
import os
from discord.ext import commands
import youtube_dl
import psycopg2
from queries import *

coin = [':disguised_face:', ':peach:']

special_user = 417772375199711242

#default insultls
# starter_insults = [
#     'eats cat shit.',
#     'is more disappointing than an unsalted pretzel.',
#     'is impossible to underestimate.',
#     'wears a mask, but not for covid.',
#     'has a nugget fetish.',
#     'is a test tube baby.',
#     'ass is jealous of the amount of shit that comes out of their mouth.',
#     'is a troggy.',
# ]

client = commands.Bot(command_prefix='.', intents = discord.Intents.all())

#bot ready confirmation
@client.event
async def on_ready():
    print(f'logged on as {client.user}!')

#message check features
@client.listen('on_message')
async def messages(ctx):
    #url regex
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ctx.content.lower())

  #checks if bot says 69
    if ctx.author == client.user:
        if '69' in ctx.content:
            temp_list = ctx.content.split(' ')
            for i in temp_list:
                if len(re.findall('<.*>', i)) > 0:
                    temp_list.remove(i)
            temp_list = ' '.join([str(i) for i in temp_list])
            if '69' in temp_list:
                await ctx.channel.send('nice')
        return

    #checks if user says 69
    if '69' in ctx.content:
        if len(urls) >= 1:
            return
    else:
        temp_list = ctx.content.split(' ')
        for i in temp_list:
            if len(re.findall('<.*>', i)) > 0:
                temp_list.remove(i)
                temp_list = ' '.join([str(i) for i in temp_list])
                if '69' in temp_list:
                    await ctx.channel.send('nice')

    #checks if user says fuck you
    if ctx.content.lower().startswith('fuck you'):
        for i in range(0, len(re.findall('<.*>', ctx.content))):
            if i == (len(re.findall('<.*>', ctx.content)) - 1):
                await ctx.channel.send(f'Yeah, fuck you {re.findall("<.*>", ctx.content)[i]}')

    #checks compliment for bot
    if 'good bot' in ctx.content.lower():
        await ctx.channel.send(':relieved:')

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

#play
# @client.command()
# async def play(ctx, url: str):
#     if ctx.author.voice == None:
#         await ctx.send('You must be connected to a voice channel...')
#         return
#     else:
#         voiceChannel = discord.utils.get(ctx.guild.voice_channels,
#                                          name=str(ctx.author.voice.channel))
#         voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#         if voice == None:
#             await voiceChannel.connect()
#             voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#         else:
#             await ctx.guild.voice_client.move_to(voiceChannel)

#     ydl_opts = {
#         'format':
#         'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }

#     os.chdir(str(os.getenv('main_path') + '/Temp MP3'))
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#     for file in os.listdir(os.getenv('main_path') + '/Temp MP3'):
#         if file.endswith('.mp3'):
#             os.rename(file, 'song.mp3')
#     voice.play(discord.FFmpegPCMAudio('song.mp3'))
#     os.chdir('./')


#pauses audio
# @client.command(name='pause')
# async def pause(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_playing():
#         voice.pause()
#     else:
#         await ctx.send('No audio is playing...')


#resume
# @client.command(name='resume')
# async def resume(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_paused():
#         voice.resume()
#     else:
#         await ctx.send('Audio is currently playing...')


#stop
# @client.command()
# async def stop(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     voice.stop()


#disconnect
# @client.command()
# async def leave(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice == None:
#         await ctx.send("I'm not connected")
#     elif voice.is_connected():
#         await voice.disconnect()


# @client.command()
# async def test(ctx):
#   # print(re.findall('<.*>', ctx.author))
#   print(re.findall('<.*>', ctx.message.content))

#thornberry
# @client.command()
# async def donny(ctx):
#     sound_byte = []
#     if ctx.author.voice == None:
#         await ctx.send('You must be connected to a voice channel...')
#     else:
#         voiceChannel = discord.utils.get(ctx.guild.voice_channels,
#                                          name=str(ctx.author.voice.channel))
#         voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#         if voice == None:
#             await voiceChannel.connect()
#             voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#         else:
#             await ctx.guild.voice_client.move_to(voiceChannel)
#     if os.getcwd() != os.getenv('main_path') + '/Thornberry':
#         os.chdir(str(os.getenv('main_path') + '/Thornberry'))
#     for file in os.listdir(os.getcwd()):
#         if file.endswith('.mp3'):
#             sound_byte.append(file)
#     voice.play(discord.FFmpegPCMAudio(random.choice(sound_byte)))
#     while voice.is_playing():
#         pass
#     if voice.is_connected():
#         await voice.disconnect()
#     os.chdir(os.getenv('main_path'))

#gopnik
# @client.command()
# async def gopnik(ctx):
#   if ctx.author.voice == None:
#       await ctx.send('You must be connected to a voice channel...')
#   else:
#       voiceChannel = discord.utils.get(ctx.guild.voice_channels,
#                                         name=str(ctx.author.voice.channel))
#       voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#       if voice == None:
#           await voiceChannel.connect()
#           voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#       else:
#           await ctx.guild.voice_client.move_to(voiceChannel)
#   if os.getcwd() != os.getenv('main_path') + '/Gop':
#       os.chdir(str(os.getenv('main_path') + '/Gop'))
#   for file in os.listdir(os.getcwd()):
#       if file.endswith('.mp3'):
#         voice.play(discord.FFmpegPCMAudio(file))
#   while voice.is_playing():
#       pass
#   if voice.is_connected():
#       await voice.disconnect()
#   os.chdir(os.getenv('main_path'))

@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command(hidden=True)
async def unload(ctx, extension):
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

