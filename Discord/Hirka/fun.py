import discord
from discord.ext import commands
import requests
import inspect


bot = commands.Bot(command_prefix = ";") #Initialise client bot  

class fun():
    def __init__(self,bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def debug(self, ctx, *, code : str):
        """Evaluates code."""
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

def setup(bot):
    bot.add_cog(fun(bot))
