from discord.ext import commands
import random

class Chance(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.coin = [':disguised_face:', ':peach:']
    
    #coin flip
    @commands.command(name='coin', help='Flip a coin')
    async def flip(self, ctx):
        await ctx.send(random.choice(self.coin))


    #d20
    @commands.command(name='d20', help='Roll a d20')
    async def roll(self, ctx):
        await ctx.send(random.randint(1, 20))    

def setup(client):
    client.add_cog(Chance(client))
