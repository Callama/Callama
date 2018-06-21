import discord
from discord.ext import commands
import logging
import sys





description = '''Hirka Bot created by @Callama'''
bot = commands.Bot(command_prefix=';', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
	bot.load_extension('fun')
	bot.load_extension('general')
    await bot.change_presence(game=discord.Game(name=';help'))
    
   


    
# Loads modules manually for testing and whatnot
@bot.command(pass_context=True, hidden="True")
async def load(ctx, extension_name:str):
	if ctx.message.author.id == "160847568488628225":
	    try:
	        bot.load_extension(extension_name)
	    except (AttributeError, ImportError) as e:
	        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
	        return
	    await bot.say("`{}`  has been loaded.".format(extension_name))
	else:
		await bot.say("You do not have permission to load/unload cogs")

# Unloads for whatever reason
@bot.command(pass_context=True, hidden=True)
async def unload(ctx, extension_name:str):
	if ctx.message.author.id == "160847568488628225":
	    bot.unload_extension(extension_name)
	    await bot.say("{} unloaded.".format(extension_name))
	else:
		await bot.say("You do not have permission to load/unload cogs")

# Refreshes modules because unloading and then loading is work for peasents.
@bot.command(pass_context=True, hidden=True)
async def refresh(ctx, extension_name:str):
	if ctx.message.author.id == "160847568488628225":
		bot.unload_extension(extension_name)
		bot.load_extension(extension_name)
		await bot.say("Module refreshed")
	else:
		await bot.say("You don't have permission to refresh this module")

 



bot.run('NDU2OTc3NzA3MTU1MTkzODY3.DgSZLA.GEzfKv_H9AC2VG6_NDUOzRNTG68')


    


        



