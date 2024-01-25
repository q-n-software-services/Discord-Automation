import discord
import random

TOKEN = "MTAxMjI5OTIxNzQyMDY4NTM1NA.GlC1DI.TGO2OExuWwm4XEZsMhi_pF9w43eMzFdcmCPgpc"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)



