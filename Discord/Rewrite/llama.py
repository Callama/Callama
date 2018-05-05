import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "tl!") #Initialise client bot        

class llama():
    def __init__(self, bot):
        self.bot = bot
    @bot.command(pass_context=True)
    async def llamagif(self,ctx):
        await self.bot.say("https://cdn.discordapp.com/attachments/428651218093473795/438801901493157919/Callama.gif")
    @bot.command(pass_context=True)
    async def llama(self,ctx):
        await self.bot.say('Llamas are Fabulous! <:llama:438103417773096961>')
def setup(bot):
    bot.add_cog(llama(bot))