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

startup_extensions = ["games","llama"]

bot = commands.Bot(command_prefix = "tl!") #Initialise client bot
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Da Llama is ready!")
    await bot.change_presence(game=discord.Game(name='a Llama thing'))

@bot.command()
async def load(ctx,extension_name : str):
    """Loads an extension."""
    if ctx.message.author.id.startswith('160847568488628225'):
        try:
            bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await bot.say("{} Has been loaded!".format(extension_name))


@bot.command()
async def unload(ctx,extension_name : str):
    """Unloads an extension."""
    if ctx.message.author.id.startswith('160847568488628225'):
        bot.unload_extension(extension_name)
        await bot.say("{} Has been unloaded!".format(extension_name))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@bot.command(hidden=True, pass_context=True)
async def reload( ctx, extension_name : str):
    """Reloads an extension."""
    if ctx.message.author.id.startswith('160847568488628225'):
        bot.unload_extension(extension_name)
        bot.load_extension(extension_name)
        await bot.say("{} has been reloaded!".format(extension_name))
        print("{} has been reloaded!".format(extension_name))

            
            

bot.run("NDQxNzExNDA4NzY2NTE3MjU5.Dc0PUw.VRfkuF_gzXT1pQRTz8hN5hv6sFU")



