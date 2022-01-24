import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! (round(client.latency * 1000))ms')

@client.event
async def on_member_join(member):
    print(f'(member) has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'(member) has left a server.')

client.run('OTM1MDc3Mzc2Nzc2MzU1ODgw.Ye5Yqw.ch008SJKoSLVKWFFasYA8hvDpuM')
