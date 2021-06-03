from discord.ext import commands
import random
import re

class Bitch(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #bitch calculation command
    @commands.command(name='hmb', help='Calculates how much bitch someone is.')
    async def hmb(self, ctx, message):
        percentage = random.randint(0, 101)
        if percentage >= 95:
            percentage = random.randint(95, 151)
        await ctx.send(
            re.findall('<.*>', message)[0] + f' is {percentage}% bitch...')

def setup(client):
    client.add_cog(Bitch(client))
