import discord
from discord.ext import commands
import imgurpython
import TOKEN
import giphypop
bot = commands.Bot(command_prefix = ";") #Initialise client bot  

GIPHY_TOKEN = TOKEN.giphy


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

    



def setup(bot):
    bot.add_cog(links(bot))