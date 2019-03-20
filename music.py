import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping():
     await ctx.send('Pong!')
@bot.command()
async def mul(ctx, num1: int, num2: int):
     await ctx.send(num1*num2)

@bot.event
async def on_ready():
    game = discord.Game("with the Api")
    await bot.change_presence(status=discord.Status.idle, activity=game)



bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
