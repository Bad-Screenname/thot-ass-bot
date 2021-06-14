from discord.ext import commands
from twilio.rest import Client
import os

class Feature(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.msg_client = Client(os.getenv('twilio_sid'), os.getenv('twilio_token'))

    @commands.command(name='request', help='use this command to ask me to add a new feature')
    async def request(self, ctx):
        text_msg = self.msg_client.messages.create(
            body = f'{ctx.author.name} asks "{ctx.content.split(".request")[1]}"',
            from_ = os.getenv('twilio_number'),
            to = os.getenv('my_number')
        )

def setup(client):
    client.add_cog(Feature(client))