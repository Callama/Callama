import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import sys
import os
import random
import urllib.request
import json

Client = discord.Client() #Initialise Client 
bot = commands.Bot(command_prefix = "r!") #Initialise client bot
bot.remove_command('help')

@bot.event
async def on_ready():
    print("DA POTATO IS RIPE AND READY")
    await bot.change_presence(game=discord.Game(name='Pokemon'))
@bot.command(pass_context=True)
async def totodile(ctx):
    await bot.say("Totodiles are totolly tubular!")


@bot.command(pass_context=True)
async def restart(ctx):
    if ctx.message.author.id.startswith('160847568488628225'):
        await bot.say('The Brotatoes are Restarting the Bot..')
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        await bot.say("The Brotatoes don't like that you ate there Uncle Fry")

bot.run("NDM3MDcxMzMyNzE5NzIyNTA2.Dbwvpg.VsQ-VvWx88SdYwGehzPgKprDoWY")
