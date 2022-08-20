import discord
from discord.ext import commands
from asyncio import *
from config import PREFIX, TOKEN


client = commands.Bot(command_prefix=PREFIX, help_command=None)


@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def ping(ctx):
    await ctx.reply("Pong!")

@client.command()
async def avatar(ctx):
    mention = ctx.author.mention
    avatar = ctx.author.avatar_url
    await ctx.send(avatar)
    await ctx.replay(f"{mention}, This is your profile picture!")



client.run(TOKEN)