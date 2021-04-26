#!/bin/python3
import os
import discord
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

utilities.bot_init()
client.run(os.getenv('DISCORD_TOKEN'))
