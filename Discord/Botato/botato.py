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





bot.run("NDM3MDcxMzMyNzE5NzIyNTA2.Dbwvpg.VsQ-VvWx88SdYwGehzPgKprDoWY")
