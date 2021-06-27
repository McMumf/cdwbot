#!/bin/python3
import os
import discord
from discord.ext import tasks
import json
import functions, utilities

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == os.getenv('DISCORD_SERVER'):
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@tasks.loop(hours = 24)
async def birthdayLoop():

    for guild in client.guilds:
        if guild.name == os.getenv('DISCORD_SERVER'):
            channel = discord.utils.get(guild.channels, name = 'general')

            for user in functions.check_birthdays():
                await channel.send("Happy Birthday, " + user + "!!!")

            break



# This is where you put the commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$dave'):
        # Caution, Profanity
        msg = "Fuck you, Dave"
        await message.channel.send(msg)

    if message.content.startswith('$bday'):
        msg = functions.birthday_controller(message)
        await message.channel.send(msg)

birthdayLoop.start()

utilities.bot_init()
client.run(os.getenv('DISCORD_TOKEN'))
