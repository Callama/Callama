import discord
from discord.ext import commands
import imgurpython
import TOKEN
import giphypop
import requests
from weather import Weather, Unit
import pyowm
from urllib.parse import quote
from urllib.request import urlopen
bot = commands.Bot(command_prefix = ";") #Initialise client bot  

GIPHY_TOKEN = TOKEN.giphy

owm = pyowm.OWM(TOKEN.weather)
class links():
    def __init__(self,bot):
        self.bot = bot

        @bot.command(pass_context=True)
        async def gif(ctx, *args):
            """
            A simple command to send gifs by keyword from giphy api
            """
            if args:
                query = " ".join(args)
                index = 0
                if " -" in query:
                    try:
                        index = int(query.split(" -")[1])
                    except:
                        pass
                    query = query.split(" -")[0]
                giphy = giphypop.Giphy() if GIPHY_TOKEN == "" else giphypop.Giphy(api_key=GIPHY_TOKEN)
                gif = [x for x in giphy.search(query)][index]
                if gif:
                    await self.bot.say(gif)
            await bot.delete_message(ctx.message)
            return gif

        @bot.command(pass_context=True)
        async def weather(self,ctx,*,place = None):
            weathers = Weather(Unit.CELSIUS)
            location = weathers.lookup_by_location(place)
            condition = location.condition
            await self.bot.say(condition.text)
            return weather 

        @bot.command(pass_context=True)
        async def lmgtfy(self,ctx,*,search = None):
            """Search...Stuff I guess"""

            if search == None:
                await self.bot.say('You need to enter a query!')

            lmgtfyl = "http://lmgtfy.com/?q={}".format(quote(search))
            lmgtfyt = tiny_url(lmgtfyl)
            await self.bot.say('You can find your answers here:\n\n<{}>'.format(lmgtfyt))
            return lmgtfy
            #WORK ON
        @bot.command(pass_context=True)
        async def tinyurl(self,ctx,link : str):
            tinyurl2 = tiny_url(link)
            await self.bot.say('Your link is: {}'.format(tinyurl2))
            




        def tiny_url(url):
            """Convert Url to Tiny Url and return url"""
            apiurl = "http://tinyurl.com/api-create.php?url="
            tinyurl = urlopen(apiurl + url).read().decode("utf-8")
            return tinyurl

        #End Work On
        

        


            


            

    
            
            



    



def setup(bot):
    bot.add_cog(links(bot))