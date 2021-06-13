from discord.ext import commands
import os
import youtube_dl
from discord import utils
import discord
import ffmpeg

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client
    
#play
    # @commands.command()
    # async def play(self, ctx, url: str):
    #     if ctx.author.voice == None:
    #         await ctx.send('You must be connected to a voice channel...')
    #         return
    #     else:
    #         voiceChannel = discord.utils.get(ctx.guild.voice_channels,
    #                                          name=str(ctx.author.voice.channel))
    #         voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
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

    #ussr
    @commands.command()
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
      os.chdir('./audio/ussr')
      for file in os.listdir(os.getcwd()):
          if file.endswith('.mp3'):
            voice.play(discord.FFmpegPCMAudio(file))
      while voice.is_playing():
          pass
      if voice.is_connected():
          await voice.disconnect()
          os.chdir('/app/')


    #thornberry
    @commands.command()
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
      os.chdir('./audio/thornberry')
      for file in os.listdir(os.getcwd()):
          if file.endswith('.mp3'):
            voice.play(discord.FFmpegPCMAudio(file))
      while voice.is_playing():
          pass
      if voice.is_connected():
          await voice.disconnect()
          os.chdir('/app/')

    #gopnik
    @commands.command()
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
      os.chdir('./audio/gopnik')
      for file in os.listdir(os.getcwd()):
          if file.endswith('.mp3'):
            voice.play(discord.FFmpegPCMAudio(file))
      while voice.is_playing():
          pass
      if voice.is_connected():
          await voice.disconnect()
          os.chdir('/app/')

def setup(client):
    client.add_cog(Voice(client))