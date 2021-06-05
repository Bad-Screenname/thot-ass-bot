from discord.ext import commands
import re

class Messages(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener('on_message')
    async def messages(self, ctx):
    #url regex
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ctx.content.lower())

    #checks if bot says 69
        if ctx.author == self.client.user:
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
        if '69' in ctx.content.lower() and len(urls) >= 1: 
            return
        elif '69' in ctx.content.lower():
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

def setup(client):
    client.add_cog(Messages(client))
