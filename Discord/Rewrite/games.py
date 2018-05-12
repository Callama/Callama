import discord
from discord.ext import commands
import random
import time

bot = commands.Bot(command_prefix = "tl!") #Initialise client bot 

class games():
    def __init__(self, bot):
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



def setup(bot):
    bot.add_cog(games(bot))

        

        



    