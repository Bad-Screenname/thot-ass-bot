from discord.ext import commands
import os
import youtube_dl
from discord import utils
import discord

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client
    
#play
    @commands.command()
    async def play(self, ctx, #url: str):
    ):
        if ctx.author.voice == None:
            await ctx.send('You must be connected to a voice channel...')
            return
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels,
                                             name=str(ctx.author.voice.channel))
            voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
            if voice == None:
                await voiceChannel.connect()
                voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
            else:
                await ctx.guild.voice_client.move_to(voiceChannel)

        ydl_opts = {
            'format':
            'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        print(os.getcwd())
        # os.chdir(str(os.getenv('main_path') + '/Temp MP3'))
        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #     ydl.download([url])
        # for file in os.listdir(os.getenv('main_path') + '/Temp MP3'):
        #     if file.endswith('.mp3'):
        #         os.rename(file, 'song.mp3')
        # voice.play(discord.FFmpegPCMAudio('song.mp3'))
        # os.chdir('./')

def setup(client):
    client.add_cog(Voice(client))