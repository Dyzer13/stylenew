import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client() 
client = commands.Bot(command_prefix = ">")

@client.event 
async def on_ready():
Game = discord.Game("with me")
await bot.change_presence(status=discord.Status.idle, activity=game)



client.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
