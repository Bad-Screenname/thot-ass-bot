from discord.ext import commands
import os
import youtube_dl
from discord import utils
import discord
import ffmpeg

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.main_path = '/app/'
    
# #play
    # @commands.command()
#     async def play(self, ctx, url: str):
#         if ctx.author.voice == None:
#             await ctx.send('You must be connected to a voice channel...')
#             return
#         else:
#             voiceChannel = discord.utils.get(ctx.guild.voice_channels,
#                                              name=str(ctx.author.voice.channel))
#             voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
#             if voice == None:
#                 await voiceChannel.connect()
#                 voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
#             else:
#                 await ctx.guild.voice_client.move_to(voiceChannel)

#         ydl_opts = {
#             'format':
#             'bestaudio/best',
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',
#             }],
#         }

#         os.chdir(str('/app/audio/temp_mp3/'))
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         for file in os.listdir('/app/audio/temp_mp3/'):
#             if file.endswith('.mp3'):
#                 os.rename(file, 'song.mp3')
#         voice.play(discord.FFmpegPCMAudio('song.mp3'))
#         while voice.is_connected():
#             if not voice.is_playing():
#                 await voice.disconnect()
#                 os.chdir('/app/')
    
#     #pauses audio
#     @commands.command(name='pause')
#     async def pause(self, ctx):
#         voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
#         if voice.is_playing():
#             voice.pause()
#         else:
#             await ctx.send('No audio is playing...')

#     #resume
#     @commands.command(name='resume')
#     async def resume(self, ctx):
#         voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
#         if voice.is_paused():
#             voice.resume()
#         else:
#             await ctx.send('Audio is currently playing...')

#     #stop
#     @commands.command()
#     async def stop(self, ctx):
#         voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
#         voice.stop()
    
#     #disconnect
#     @commands.command()
#     async def leave(self, ctx):
#         voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
#         if voice == None:
#             await ctx.send("I'm not connected")
#         elif voice.is_connected():
#             await voice.disconnect()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.id == 184874380969377792:
            if before.channel is None and after.channel is not None:
                voiceChannel = await after.channel.connect()
                voice = member.guild.voice_client

                
                os.chdir('./audio/ussr/')
                for file in os.listdir(os.getcwd()):
                    if file.endswith('.mp3'):
                        voiceChannel.play(discord.FFmpegPCMAudio(file))
                        print('1')
                while voice.is_connected():
                    if not voice.is_playing():
                        print('3')
                        await voice.disconnect()
                        print('4')
                os.chdir('/app/')
                print('5')
        else:
            print('failed')
            pass

    #ussr
    @commands.command(help="National Anthem")
    async def ussr(self, ctx):
      if ctx.author.voice == None:
          await ctx.send('You must be connected to a voice channel...')
      else:
          voiceChannel = discord.utils.get(ctx.guild.voice_channels,
                                            name=str(ctx.author.voice.channel))
          voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
          if voice == None:
              await voiceChannel.connect()
              voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
          else:
              await ctx.guild.voice_client.move_to(voiceChannel)
      os.chdir('/app/audio/ussr')
      for file in os.listdir(os.getcwd()):
          if file.endswith('.mp3'):
            voice.play(discord.FFmpegPCMAudio(file))
      while voice.is_connected():
          if not voice.is_playing():
              await voice.disconnect()
              os.chdir('/app/')


    #thornberry
    @commands.command(help="Donny Thornberry")
    async def donny(self, ctx):
      if ctx.author.voice == None:
          await ctx.send('You must be connected to a voice channel...')
      else:
          voiceChannel = discord.utils.get(ctx.guild.voice_channels,
                                            name=str(ctx.author.voice.channel))
          voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
          if voice == None:
              await voiceChannel.connect()
              voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
          else:
              await ctx.guild.voice_client.move_to(voiceChannel)
      os.chdir('/app/audio/thornberry')
      for file in os.listdir(os.getcwd()):
          if file.endswith('.mp3'):
            voice.play(discord.FFmpegPCMAudio(file))
      while voice.is_connected():
          if not voice.is_playing():
              await voice.disconnect()
              os.chdir('/app/')

    #gopnik
    @commands.command(help="Gopnik by DJ Blyatman")
    async def gopnik(self, ctx):
      if ctx.author.voice == None:
          await ctx.send('You must be connected to a voice channel...')
      else:
          voiceChannel = discord.utils.get(ctx.guild.voice_channels,
                                            name=str(ctx.author.voice.channel))
          voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
          if voice == None:
              await voiceChannel.connect()
              voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
          else:
              await ctx.guild.voice_client.move_to(voiceChannel)
      os.chdir('/app/audio/gopnik')
      for file in os.listdir(os.getcwd()):
          if file.endswith('.mp3'):
            voice.play(discord.FFmpegPCMAudio(file))
      while voice.is_connected():
          if not voice.is_playing():
              await voice.disconnect()
              os.chdir('/app/')

def setup(client):
    client.add_cog(Voice(client))