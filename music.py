import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')
@bot.event
async def on_ready():
 await client.change.presence(game=discord.Game(name='Test'))
 print('bot is ready')

bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
