import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import bot
import random

client = commands.Bot(command_prefix = ";")


#Starting Bot
@client.event
async def on_ready():
    print("Bot is Online.")

@client.command()
async def no(ctx):
    await ctx.send('yes')

#Picture
@client.command()
async def BOP(ctx):
    await ctx.send(file=discord.File('daequan.jpg'))

@client.command()
async def cookie(ctx):
    message = await ctx.send('Locating Cookie....')
    asyncio.sleep(10.0)
    await message.edit(content='Found Cookie! :cookie:')

@client.command()
async def ping(ctx, user: discord.User, *, message=None):
    message = "Just a little message, have a good day!"
    await user.send(message)

@client.command()
async def more(ctx):
    await ctx.send("Current Commands are cookie, BOP, no, ping, randomnum.")

@client.command()
async def secret(ctx):
    await ctx.send("do ;noods :flushed:")

@client.command()
async def randomnum(ctx):
    await ctx.send(random.randrange(1,100))

@client.command()
async def noods(ctx):
    await ctx.send("https://tenor.com/view/caught-in-4k-caught-in4k-chungus-gif-19840038")
    
client.run('TOKEN')
