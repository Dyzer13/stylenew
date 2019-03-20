import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')


@bot.command()
 async def on_message(message)
       if "DyzerYT" in message.content.lower():
           await message.channel.send("https://www.youtube.com/channel/UC6Zwte0sirqK2oAoy3AaBbA/videos")
           await bot.process_commands(message)

bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
