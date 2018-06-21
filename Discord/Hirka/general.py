import discord
from discord.ext import commands
import requests
import pendulum

bot = commands.Bot(command_prefix = "!") #Initialise client bot
bot.remove_command('help')

class general():
    def __init__(self, bot):
        self.bot = bot
   

    @bot.command(pass_context=True)
    async def ping(self,ctx):
        """To see if the bot is working/how fast"""
        await self.bot.say("Pong!")


    @bot.command(pass_context=True)
    async def help(self,ctx):
        """To see all the commands, and what they do"""
        embed = discord.Embed(title=":question: Need some help?", color=0x00ff00)
        embed.add_field(name=';about',value='Who is Hirka?',inline=True)
        embed.add_field(name=";ping",value="Am I here?",inline=True)
        await self.bot.say(embed=embed)


    @bot.command(pass_context=True)
    async def about(self,ctx):
        """Info about the bot""" 
        embed = discord.Embed(title="About", color=0x00ff00)
        embed.add_field(name="Creator",value="Callama")
        await self.bot.say(embed=embed)       






def setup(bot):
    bot.add_cog(general(bot))