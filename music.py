import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
@bot.command()
async def names(ctx, name):
    ': Searched someones name'
    files = ["File1.txt", "File2.txt"]
    for i in files:
        mc = open(i).readlines()
    match = next((line for line in mc if name.lower() in line.lower()), None) # this returns the first line that has the provided name inside i
    embed = discord.Embed(title=f'''{ctx.author} Searched Name''',  description=f'''{match}''', color=discord.Colour.blue())
    await ctx.send(embed=embed)
    
    @bot.command()
async def uuid(ctx, theirname):
    """: Search NameMC"""
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://api.mojang.com/profiles/minecraft/{theirname}') as r:
            res = await r.json()
            await ctx.channel.send(res['value'])

Ignoring exception in command uuid:
Traceback (most recent call last):
  File "C:\Users\BigBoss2\PycharmProjects\DiscordBot\venv\lib\site-packages\discord\ext\commands\core.py", line 62, in wrapped
    ret = yield from coro(*args, **kwargs)
  File "C:/Users/BigBoss2/PycharmProjects/DiscordBot/Bot1.py", line 300, in uuid
    await ctx.channel.send(res['value'])
KeyError: 'value'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\BigBoss2\PycharmProjects\DiscordBot\venv\lib\site-packages\discord\ext\commands\bot.py", line 886, in invoke
    yield from ctx.command.invoke(ctx)
  File "C:\Users\BigBoss2\PycharmProjects\DiscordBot\venv\lib\site-packages\discord\ext\commands\core.py", line 498, in invoke
    yield from injected(*ctx.args, **ctx.kwargs)
  File "C:\Users\BigBoss2\PycharmProjects\DiscordBot\venv\lib\site-packages\discord\ext\commands\core.py", line 71, in wrapped
    raise CommandInvokeError(e) from e
discord.ext.commands.errors.CommandInvokeError: Command raised an exception: KeyError: 'value'


bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
