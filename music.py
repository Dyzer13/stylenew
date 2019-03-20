import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
bot.command()
async def names(ctx, name):
    ': Searched someones name'
    files = ["File1.txt", "File2.txt"]
    for i in files:
        mc = open(i).readlines()
    match = next((line for line in mc if name.lower() in line.lower()), None) # this returns the first line that has the provided name inside i
    embed = discord.Embed(title=f'''{ctx.author} Searched Name''',  description=f'''{match}''', color=discord.Colour.blue())
    await ctx.send(embed=embed)

bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
