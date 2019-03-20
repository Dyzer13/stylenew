import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
