import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')


@bot.event 
async def on_ready():
game = discord.Game ("with the api")
await client.change_presence(status=discord.Status.idle, activity=game)


bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
