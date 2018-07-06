import discord
from discord.ext import commands
import ast
from discord.ext import commands
import asyncio
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io

bot = commands.Bot(command_prefix = "!") #Initialise client bot

class owner():
    def __init__(self,bot):
        self.bot = bot


    @bot.command(pass_context=True)
    async def eval(self, ctx, *, code : str):
        """Evaluates code."""
        if ctx.message.author.id == "160847568488628225":
            code = code.strip('` ')
            python = '```py\n{}\n```'
            result = None

            env = {
                'bot': self.bot,
                'ctx': ctx,
                'message': ctx.message,
                'server': ctx.message.server,
                'channel': ctx.message.channel,
                'author': ctx.message.author
            }

            env.update(globals())

            try:
                result = eval(code, env)
                if inspect.isawaitable(result):
                    result = await result
            except Exception as e:
                await self.bot.say(python.format(type(e).__name__ + ': ' + str(e)))
                return
            try:
                await self.bot.say(python.format(result))
            except discord.HTTPException:
                await self.bot.say("Result is too long for me to send")
            except:
                pass

    

    @bot.command(pass_context=True)
    async def shutdown(self,ctx):
        """Shutsdown the bot"""
        if ctx.message.author.id == '160847568488628225':
            await self.bot.say("Shutting down...Cya Callama!")
            await bot.logout()
        else:
            await self.bot.say(":no: You do not have permission to shutdown Hirka.")

    @bot.command(pass_context=True, aliases=['listen', 'watch'])
    async def play(self,ctx, *, media_title: str):
        if ctx.message.author.id == '160847568488628225':
            """Update my presence."""
            p_types = {'play': 0, 'listen': 2, 'watch': 3}
            my_media = discord.Game(name=media_title, type=p_types[ctx.invoked_with])
            await self.bot.change_presence(game=my_media)
        else:
            await self.bot.say(":no: You may not use this command.")
    
    


    
        

    
    
            




def setup(bot):
    bot.add_cog(owner(bot))