import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client() #Initialise Client 
bot = commands.Bot(command_prefix = "!") #Initialise client bot
bot.remove_command('help')


@bot.event
async def on_ready():
    print("The Bot is online")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say('PONG')

bot.run("PUT TOKEN HERE")
