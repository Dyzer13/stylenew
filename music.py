import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')


@bot.event()
async def on_ready():
    await bot.change_presence(activity=discord.streaming(name="waiting", url="https://www.twitch.tv/clow")) 
bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
