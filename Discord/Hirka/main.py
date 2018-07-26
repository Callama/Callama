import discord
from discord.ext import commands 
import logging
import sys
import TOKEN
import json
from datetime import datetime




description = '''Hirka Bot created by @Callama'''
bot = commands.Bot(command_prefix=';', description=description)
bot.remove_command('help')

bot.launch_time = datetime.utcnow()
#Basic Logging
logging.basicConfig(level=logging.WARNING)
@bot.event
async def on_ready():
	print("Loaded")
	bot.load_extension('fun')
	bot.load_extension('general')
	bot.load_extension('owner')
	bot.load_extension('links')
	bot.load_extension('dbs')
	bot.load_extension('music')

with open ('data/blacklist.json') as bl:
	blacklist = json.load(bl)["users"]








    
   

@bot.command(pass_context=True)
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await bot.say(f"{days}d, {hours}h, {minutes}m, {seconds}s")
    
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
		await bot.say(":no: You do not have permission to load/unload cogs")



# Unloads for whatever reason
@bot.command(pass_context=True, hidden=True)
async def unload(ctx, extension_name:str):
	if ctx.message.author.id == "160847568488628225":
	    bot.unload_extension(extension_name)
	    await bot.say("{} unloaded.".format(extension_name))
	else:
		await bot.say(":no: You do not have permission to load/unload cogs")

# Refreshes modules because unloading and then loading is work for peasents.
@bot.command(pass_context=True, hidden=True)
async def refresh(ctx, extension_name:str):
	if ctx.message.author.id == "160847568488628225":
		bot.unload_extension(extension_name)
		bot.load_extension(extension_name)
		await bot.say("Module refreshed")
	else:
		await bot.say(":no: You don't have permission to refresh this module")

 


#Token
bot.run(TOKEN.token)



    


        



