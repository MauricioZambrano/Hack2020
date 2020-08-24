import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


# This gives you a message to let you know that the bot is on
@client.event
async def on_ready():
    print('Bot is ready.')
# This lets you know in the console when someone has joined
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

# This lets you know in the console when someone has left
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

#comand for getting the info about the bot
@client.command()
async def info(ctx):
    await ctx.send(f'This is the Hackaton 2020 bot under going development {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

client.run('NzQ2NzY4NDAwOTkwMzM5MTAy.X0FIRQ.JoWwX4TKZ1CdxVi_jwaBu06b9bc')