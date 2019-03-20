import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
    @client.command(pass_context=True)
async def kick(ctx, member: discord.Member = None):
    channel = ctx.message.channel
    message = ctx.message
    if not member:
        await client.send_message(ctx.message.channel, 'Please specify a member')
        return
    await client.kick(member)
    await client.say('{} got kicked'.format(member.mention))
    await client.delete_message(message)

bot.run('NTU3ODM5ODcxNzQyNTc0NjE0.D3ONFQ.bw60zevXJO-k28s08Te_aeWh_qo')
