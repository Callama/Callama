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
    
    @bot.group(pass_context=True, invoke_without_command=True)
    async def help(self,ctx):
        """To see all the commands, and what they do"""
        embed = discord.Embed(title='``There are 3 command modules``', color=0x00ff00)
        embed.add_field(name='Modules',value='```•Fun\n•Links\n•General```\nUse ;help (Module) to see commands')
        await self.bot.say(embed=embed)
        
    @help.command(pass_context=True)
    async def admin(self,ctx):
        embed = discord.Embed(title="Bot-Admin Commands",color=0x00ff00)
        embed.add_field(name=';eval',value='Evalualte Code/Maths',inline=True)
        embed.add_field(name=';shutdown',value='Shutdown the Bot',inline=True)
        await self.bot.say(embed=embed)
    
    @help.command(pass_context=True)
    async def fun(self,ctx):
        embed = discord.Embed(title="Fun Commands",color=0x00ff00)
        embed.add_field(name=';coinflip',value='Heads or Tails?')
        embed.add_field(name=';dice',value='Wip')
        embed.add_field(name=';insult (person)',value='Insult somebody!')
        await self.bot.say(embed=embed)



    @help.command(pass_context=True)
    async def general(self,ctx):
        embed = discord.Embed(title="General Commands",color=0x00ff00)
        embed.add_field(name=';ping',value='See the ping of Hirka!')
        embed.add_field(name=';uptime',value='See how long Hirka has been online')
        embed.add_field(name=';servers',value='How many servers am I in?')
        embed.add_field(name=';status',value='See Discords status')
        embed.add_field(name=';say',value='Make the bot say somthing!')
        await self.bot.say(embed=embed)

    @help.command(pass_context=True)
    async def links(self,ctx):
         embed = discord.Embed(title="Link Commands",color=0x00ff00)
         embed.add_field(name=';gihpy (args)',value='Get a Gif!')
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
        await self.bot.say(":ping_pong: Pong! ``{}ms``".format(round((t2-t1)*1000)))
        
    

    
    @bot.command(pass_context=True, no_pm=True)
    async def avatar(self,ctx, member: discord.Member = None):
        """User Avatar"""
        if member is None:
            author = ctx.message.author
            avatar = author.avatar_url
            e = discord.Embed(title="{}'s avatar".format(author),color=0x00ff00)
            e.set_image(url=avatar)
            e.set_footer(text=f'Requested by {ctx.message.author.name}',icon_url=avatar)
            await self.bot.say(embed=e)

        else:
            avatar = member.avatar_url
            e = discord.Embed(title="{}'s avatar".format(member),color=0x00ff00)
            e.set_image(url=avatar)
            e.set_footer(text=f'Requested by {ctx.message.author.name}',icon_url=avatar)
            await self.bot.say(embed=e)
            

        
        

    @bot.command(pass_context=True)
    async def invite(self,ctx):
        await self.bot.say("Invite me to your own server with this link!\n https://discordapp.com/api/oauth2/authorize?client_id=456977707155193867&permissions=0&scope=bot")
   

   
        
        
    @bot.command(pass_context=True)
    async def status(self,cxt):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://srhpyqt94yxb.statuspage.io/api/v2/status.json') as r:
                state = await r.json()
                if state['status']['description'] == 'All Systems Operational':
                    await self.bot.say('<:online:313956277808005120> {}'.format(state['status']['description']))

    @bot.command(pass_context=True)
    async def say(self,ctx,*,args):
        await self.bot.say(args)
        message = ctx.message
        await bot.delete_message(message)


def setup(bot):
    bot.add_cog(general(bot))