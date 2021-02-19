import discord
import os
from decouple import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'gather' in message.content:
        await message.channel.send('https://gather.town/app/Uu7dRIJ7BdzD44NS/party')

discordBotKey = config('TOKEN')
client.run(discordBotKey)