# bot.py

import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

with open('token.txt') as f:
    TOKEN = f.readline()

client.run(TOKEN)