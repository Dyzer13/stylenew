import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
client = Client()

COMMANDS = [
                "!Version",
                "!Owner",
           ]

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    elif message.content.startswith('!Owner'):
        embed = discord.Embed(title="The Owner is!", description="Chrome Panda", color=0x00ff00)
        await client.send_message(message.channel, embed=embed)
    elif message.content.startswith('!Version'):
        embed = discord.Embed(title="Version for this Bot is", description="Virsion = 1.0", color=0x00ff00)
        await client.send_message(message.channel, embed=embed)
    elif message.content.startswith('!COMMANDS'):
        embed = discord.Embed(title="Commands Are", description="Version, Owner", color=0x00ff00)
        await client.send_message(Message.channel, embed=embed)



@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("PandaBot is ready to use!\n\nHave Fun!")
    client.close()

bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
