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
from environmentvar import *

coin = [':disguised_face:', ':peach:']

special_user = 417772375199711242

#grabs insults from database
def fetch_insults():
    temp = []
    con = psycopg2.connect(
        user=os.getenv(DATABASE_USER),
        password=os.getenv(DATABASE_PASSWORD),
        host=os.getenv(DATABASE_HOST),
        database=os.getenv(DATABASE_ID)
    )
    cur = con.cursor()
    cur.execute(read_query())
    raw_insults = cur.fetchall()
    for _ in raw_insults:
        temp.append(''.join(_[0]))
    cur.close()
    con.close()
    return temp

def update_insults(insult):
    '''
    ??????????????????????????????????????????????????????????????????????????????????????????
    ??????????????????????????????????????????????????????????????????????????????????????????
    '''
    con = psycopg2.connect(
        user=os.getenv(DATABASE_USER),
        password=os.getenv(DATABASE_PASSWORD),
        host=os.getenv(DATABASE_HOST),
        database=os.getenv(DATABASE_ID)
    )
    cur = con.cursor()
    insults = options
    insults.append(insult)
    cur.execute(create_row_query(insult))
    cur.close()
    con.commit()
    con.close()
    return
    # if 'insults' in db.keys():
    #     insults = db['insults']
    #     insults.append(insult)
    #     db['insults'] = insults
    # else:
    #     db['insults'] = [insult]


#default instuls
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

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())


#bot ready confirmation
@client.event
async def on_ready():
    print(f'logged on as {client.user}!')

options = fetch_insults()


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
              await ctx.channel.send(
                  f'Yeah, fuck you {re.findall("<.*>", ctx.content)[i]}')

  #checks compliment for bot
  if ctx.content.lower().startswith('good bot'):
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

# bully command
@client.command(name='bully', help='Bully the user mentioned after command.')
async def bully(ctx, message):
    await ctx.send(f'{re.findall("<.*>", message)[0]} ' +
                   random.choice(options))


#list insults
@client.command(name='list_insults',
                help='Lists available insults.')
async def list_insults(ctx):
    text_message = ''
    index = 1
    await ctx.send('Insults')
    for i in range(0, len(options)):
        text_message = text_message + str(index) + '. ' + options[i] + '\n'
        index += 1
    text_message += 'end'
    await ctx.send(text_message)
    del text_message


#adds insult to database
@client.command(name='add', help='Adds given insult to the database.')
async def add(ctx, message):
    insult = "'" + ctx.message.content.lower().split('?add ')[1] + "'"
    update_insults(insult)
    await ctx.send(insult)
    await ctx.send(f'added {insult} to the list of insults...')


#deletes insult from list
# @client.command(name='delete',
#                 help='***list_insult first*** Deletes insult from list.')
# async def delete(ctx, message):
#     insults = []
#     if 'insults' in db.keys():
#         index = int(message)
#         print(index)
#         del db['insults'][index - 8]
#         insults = db['insults'].value
#         await ctx.send(insults)


#bitch calculation command
@client.command(name='hmb', help='Calculates how much bitch someone is.')
async def hmb(ctx, message):
    print(message)
    percentage = random.randint(0, 101)
    if percentage >= 95:
        percentage = random.randint(95, 151)
    await ctx.send(
        re.findall('<.*>', message)[0] + f' is {percentage}% bitch...')


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


#coin flip
@client.command(name='coin', help='Flip a coin')
async def flip(ctx):
    await ctx.send(random.choice(coin))


#d20
@client.command(name='d20', help='Roll a d20')
async def roll(ctx):
    await ctx.send(random.randint(1, 20))

@client.command()
async def test(ctx):
  # print(re.findall('<.*>', ctx.author))
  print(re.findall('<.*>', ctx.message.content))

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


# client.run(os.getenv('DISCORD_TOKEN'))
client.run('ODI1NjA5OTE1ODAzODkzNzYx.YGAbJw.L92AHPdrUL8nFKW31taB1M1RSnI')
