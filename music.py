import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client() 
client = commands.Bot(command_prefix = ">")

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    if message.content == "Money":
        await client.send_message(message.channel, ":money_with_wings:")

@client.event
async def on_message(message):
   if message.content.startswith("!ping"):
       await client.send_message(message.channel, "Pong!")



client.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
