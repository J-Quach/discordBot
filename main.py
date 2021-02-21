import discord
import os
from decouple import config
from web_bot import web_bot

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!gatherhelp':
        await message.channel.send('Here are the list of commands available:\n'
        '!gather: gather link to join\n'
        '!cena: AND HIS NAME IS JOHN CENA\n'
        '!horn: Horn noises\n'
        '!damedame: DAMEDAMEYO\n')


    if message.content == '!gather':
        await message.channel.send('https://gather.town/app/Uu7dRIJ7BdzD44NS/party')

    if message.content == '!cena':
        return

    if message.content == '!horn':
        return

    if message.content == '!damedame':
        return



discordBotKey = config('TOKEN')
web_bot()
client.run(discordBotKey)