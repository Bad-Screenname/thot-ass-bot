from discord.ext import commands
import psycopg2
# from queries import *
import random
import re
# import os

class Bully(commands.Cog):
    def __init__(self, client):
        self.client = client
#         self.options = self.fetch_insults()
        
#     def update_insults(self):
#         self.option = self.fetch_insults()

#     def fetch_insults(self):
#         temp = []
#         con = psycopg2.connect(
#             user=os.getenv('DATABASE_USER'),
#             password=os.getenv('DATABASE_PASSWORD'),
#             host=os.getenv('DATABASE_HOST'),
#             database=os.getenv('DATABASE_ID')
#         )
#         cur = con.cursor()
#         cur.execute(read_query())
#         raw_insults = cur.fetchall()
#         for _ in raw_insults:
#             temp.append(''.join(_[0]))
#         cur.close()
#         con.close()
#         return temp
    

#     def add_insults(self, insult):
#         con = psycopg2.connect(
#             user=os.getenv('DATABASE_USER'),
#             password=os.getenv('DATABASE_PASSWORD'),
#             host=os.getenv('DATABASE_HOST'),
#             database=os.getenv('DATABASE_ID')
#         )
#         cur = con.cursor()
#         insults = self.options
#         insults.append(''.join([char for char in insult if char != "'"]))
#         cur.execute(create_row_query(insult))
#         cur.close()
#         con.commit()
#         con.close()
#         return

#     # bully command
#     @commands.command(name='bully', help='Bully the user mentioned after command.')
#     async def bully(self, ctx, message):
#         await ctx.send(f'{re.findall("<.*>", message)[0]} ' +
#                     random.choice(self.options))

#     #list insults
#     @commands.command(name='list_insults',
#                     help='Lists available insults.')
#     async def list_insults(self, ctx):
#         con = psycopg2.connect(
#             user=os.getenv('DATABASE_USER'),
#             password=os.getenv('DATABASE_PASSWORD'),
#             host=os.getenv('DATABASE_HOST'),
#             database=os.getenv('DATABASE_ID')
#         )
#         cur = con.cursor()
#         cur.execute('SELECT * FROM insults')
#         text_message = ''
#         await ctx.send('Insults')
#         for item in cur.fetchall():
#             text_message = text_message + f'id: {item[0]}\tinsult: {item[1]}\n'
#         text_message += 'end'
#         cur.close()
#         con.commit()
#         con.close()
#         await ctx.send(text_message)
#         del text_message

#     #adds insult to database
#     @commands.command(name='add', help='Adds given insult to the database.')
#     async def add(self, ctx):
#         insult = "'" + ctx.message.content.lower().split('.add ')[1] + "'"
#         print(insult)
#         self.add_insults(insult)
#         await ctx.send(f'added {insult} to the list of insults...')

#     #deletes insult from list
#     @commands.command(name='delete',
#                     help='***list_insult first*** Deletes insult from list.')
#     async def delete(self, ctx):
#         con = psycopg2.connect(
#             user=os.getenv('DATABASE_USER'),
#             password=os.getenv('DATABASE_PASSWORD'),
#             host=os.getenv('DATABASE_HOST'),
#             database=os.getenv('DATABASE_ID')
#         )
#         cur = con.cursor()
#         cur.execute(f'SELECT insult FROM insults WHERE id = {ctx.message.content.split(" ")[1]}')
#         await ctx.send(f'deleting {cur.fetchone()[0]} from insult database...')
#         try:
#             cur.execute(f'SELECT insult FROM insults WHERE id = {ctx.message.content.split(" ")[1]}')
#             trash = cur.fetchone()[0]
#             cur.execute(delete_rows_query(f"id = {ctx.message.content.split(' ')[1]}"))
#             if trash in self.options:
#                 self.options.remove(trash)
#         except:
#             await ctx.send('an error occured... insult did not get deleted')
#         cur.close()
#         con.commit()
#         con.close()

def setup(client):
    client.add_cog(Bully(client))
