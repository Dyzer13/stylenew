import discord
import asyncio
import youtube_dl
from discord.ext import commands
from discord.utils import find
import requests as rq

bot_token=os.environ['BOT_TOKEN']
client = commands.bot(command_prefix = '+')

@client.event
async def on_ready()=
 await client.change.presence(game=discord.Game(name='Test'))
 print('bot is ready')
 

bot.run('bot_token')
