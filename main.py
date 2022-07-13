# bot.py

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", description="ShinxBot")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def hello(ctx):
    await ctx.send("hello !")


@client.command()
async def serverInfo(ctx):
    server = ctx.guild

    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)

    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name

    embed = discord.Embed(title="Server Information", url="https://github.com/ClimpyX/ShinxDiscordBot",description="",color=0x69a5ff)

    embed.set_author(name="ShinxDiscordBot", url="https://github.com/ClimpyX/ShinxDiscordBot",icon_url="https://aslangamestudio.com/tr/wp-content/uploads/2021/04/discord-mascot.png")

    embed.add_field(name=":mailbox_with_mail: Online Count", value=f"{numberOfPerson} person online",inline=False)
    embed.add_field(name=":label:  The server description", value=serverDescription,inline=False)
    embed.add_field(name=":speech_balloon: Text Channels", value=f"{numberOfTextChannels} channel available",inline=True)
    embed.add_field(name=":loud_sound: Voice Channels", value=f"{numberOfVoiceChannels} channel available",inline=True)
    embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))

    await ctx.send(embed=embed)


with open('token.txt') as f:
    TOKEN = f.readline()

client.run(TOKEN)
