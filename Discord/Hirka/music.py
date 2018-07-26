import discord
from discord.ext import commands
from random import randint
from random import choice
from enum import Enum
from urllib.parse import quote_plus
import datetime
import time
import aiohttp
import asyncio
from discord import voice_client

bot = commands.Bot(command_prefix = ";") #Initialise client bot  
class music():
    def __init__(self,bot):
        self.bot=bot


    @bot.command(pass_context=True)
    async def join(self,ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.bot.join_voice_channel(channel)
    @bot.command(pass_context = True)
    async def leave(self,ctx):
        server = ctx.message.server
        vc = self.bot.voice_client_in(server)
        await vc.disconnect(vc)
        await self.bot.say('Cya later Aligator!')





def setup(bot):
    bot.add_cog(music(bot))