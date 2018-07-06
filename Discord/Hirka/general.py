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
bot = commands.Bot(command_prefix = "!") #Initialise client bot
bot.remove_command('help')

class general():
    def __init__(self, bot):
        self.bot = bot
    
    


    @bot.command(pass_context=True)
    async def help(self,ctx):
        """To see all the commands, and what they do"""
        embed = discord.Embed(title=":question: Need some help?", color=0x00ff00)
        embed.add_field(name=';about',value='Who is Hirka?',inline=True)
        embed.add_field(name=";ping",value="Am I here?",inline=True)
        embed.add_field(name=";coinflip",value="Heads or Tails?",inline=True)
        embed.add_field(name=';servers',value='How many servers am I in?',inline=True)
        embed.add_field(name=';insult',value='I saw you...in the toilet',inline=True)
        await self.bot.say(embed=embed)
        #
    @bot.command(pass_context=True,name='helpminS')
    async def help_admin(self,ctx):
        embed = discord.Embed(title="Bot-Admin Commands",color=0x00ff00)
        embed.add_field(name=';eval',value='Evalualte Code/Maths',inline=True)
        embed.add_field(name=';shutdown',value='Shutdown the Bot',inline=True)
        await self.bot.say(embed=embed)
    @bot.command(pass_context=True)
    async def about(self,ctx):
        """Info about the bot"""
        serverCount = 0
        embed = discord.Embed(title="About", color=0x00ff00)
        embed.add_field(name="Creator",value="Callama")
        for s in self.bot.servers:
            serverCount = serverCount + 1
        embed.add_field(name='Servers',value='{} servers'.format(serverCount))
        await self.bot.say(embed=embed) 
        return s      

    @bot.command(pass_context=True)
    async def servers(self,ctx):
        serverCount = 0
        for s in self.bot.servers:
            serverCount = serverCount + 1
        await self.bot.say("I am currently in `{}`  servers!".format(serverCount))
        return s


    @bot.command(pass_context=True,aliasies=['pong'])
    async def ping(self,ctx):
        """Ping! See how fast the bot is per ms"""
        channel = ctx.message.channel
        #When the command is called
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        #When the command is sent
        t2 = time.perf_counter()
        await self.bot.say(":ping_pong: Ping! ``{}ms``".format(round((t2-t1)*1000)))
        
    @bot.command(pass_context=True)
    async def avatarss(self,ctx):
            avatars = ctx.user.avatar_url
            user = ctx.message.name
            embed = discord.Embed(title="*{}'s** Avatar".format(user),color=0x00ff00)
            embed.set_thumbnail(url=avatars)
            await self.bot.say(embed=embed)

    @bot.command(pass_context=True, no_pm=True)
    async def avatars(self,ctx, member: discord.Member = None):
        """User Avatar"""
        embed = discord.Embed(title='{}'.format(member),color=0x00f00)
        link = '<a href="{member.avatar_url}">{Avatar}</a>'
        embed.add_field(name=link,value='')
        await self.bot.say(embed=embed)
        await self.bot.say("{}".format(member.avatar_url))


    
    @bot.command(pass_context=True, no_pm=True)
    async def avatar(self,ctx, member: discord.Member):
        """User Avatar"""
        await self.bot.say("{}".format(member.avatar_url))
   

   
        
        
        
        


def setup(bot):
    bot.add_cog(general(bot))