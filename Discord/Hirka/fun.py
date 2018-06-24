import discord
from discord.ext import commands
import requests
import inspect
import random


bot = commands.Bot(command_prefix = ";") #Initialise client bot  

class fun():
    def __init__(self,bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def coinflip(self,ctx):
        r=random.randint(1,2)
        if r == 2:
            embed = discord.Embed(title="Flipping the Coin..", color=0x00ff00)
            embed.add_field(name="You landed on Heads!",value="Woo!")
            embed.set_thumbnail(url="https://image.prntscr.com/image/0aS6YbfpS8ukYOHQ8as4qQ.gif")
            await self.bot.say(embed=embed)
        else:
            embed = discord.Embed(title="Flipping the Coin..", color=0x00ff00)
            embed.add_field(name="You landed on Tails!",value="Woo!")
            embed.set_thumbnail(url="https://image.prntscr.com/image/RJneWQgwRti_Uatoyofk4w.jpg")
            await self.bot.say(embed=embed)

    @bot.command(pass_context=True)
    async def dice(self,ctx):
        r=random.randint(1,6)
        if r == 1:
           embed = discord.Embed(title="You got {}!".format(r),color=0x00ff00)
           embed.set_thumbnail(url="https://image.prntscr.com/image/5JT5lnaJQnqD4mDqzYB6uw.jpg")
           await self.bot.say(embed=embed)
        if r == 2:
            embed = discord.Embed(title="You got {}!".format(r),color=0x00ff00)
            embed.set_thumbnail(url="")
            await self.bot.say(embed=embed)
        if r == 3:
            embed = discord.Embed(title="You got {}!".format(r),color=0x00ff00)
            embed.set_thumbnail(url="")
            await self.bot.say(embed=embed)
        if r == 4:
            embed = discord.Embed(title="You got {}!".format(r),color=0x00ff00)
            embed.set_thumbnail(url="")
            await self.bot.say(embed=embed)
        if r == 5:
            embed = discord.Embed(title="You got {}!".format(r),color=0x00ff00)
            embed.set_thumbnail(url="")
            await self.bot.say(embed=embed)
        if r == 6:
            embed = discord.Embed(title="You got {}!".format(r),color=0x00ff00)
            embed.set_thumbnail(url="")
            await self.bot.say(embed=embed)

    @bot.command(pass_context=True,name="8ball")
    async def _8ball(self,ctx):
        choice = ['It is certain','As I see it, yes','It is decidedly so','Most likely','Without a doubt',' Outlook good','Yes','Yes definitely ','You may rely on it','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again',"Don't count on it",'My reply is no','My sources say no','Outlook not so good','Very doubtful']      
        outcome = random.choice(choice)
        embed = discord.Embed(title=":8ball: {} ".format(outcome),color=0x00ff00)
        await self.bot.say(embed=embed)

    

def setup(bot):
    bot.add_cog(fun(bot))
