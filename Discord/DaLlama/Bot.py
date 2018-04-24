import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import sys
import os
import random
import urllib.request
import json


Client = discord.Client() #Initialise Client 
bot = commands.Bot(command_prefix = "l!") #Initialise client bot
bot.remove_command('help')






@bot.event
async def on_ready():
    print("Da Llama is ready!")
    await bot.change_presence(game=discord.Game(name='a Llama thing'))

    


@bot.command(pass_context=True)
async def restart(ctx):
    if ctx.message.author.id.startswith('160847568488628225'):
        await bot.say('The Llamas pressed the wrong button, restarting.')
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        await bot.say("The Llama don't like you")

@bot.command(pass_context=True)
async def changelog(ctx):
    embed = discord.Embed(title="DaLlamaBot's Changelog", color=0x00ff00)
    embed.add_field(name="New Commands!",value="l!llama to get a fabulous reply! l!llamas to have allot of llamas! Do l!ping to see if our bot is online. Do l!coin to flip a Coin! Do l!dice to roll a Dice! Do l!ball <message> to use the 8ball!", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Need Some Help?", color = 0x00ff00)
    embed.add_field(name="l!llamas",value="Get a few Fab Llamas",inline=True)
    embed.add_field(name="l!llama",value="Llamas are Fab Indeed",inline=True)
    embed.add_field(name="l!dice",value="Roll a Dice :o",inline=True)
    embed.add_field(name="l!coinflip",value="Fllip a coin",inline=True)
    embed.add_field(name="l!changelog",value="See our Changellog",inline=True)
    embed.add_field(name="l!ball",value="Roll The Mysticall Ball Oo",inline=True)
    embed.set_thumbnail(url="https://image.prntscr.com/image/gdM4vN0UTxu8RBX0Ivodiw.jpg")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong! <:HappyLlama:429081444577574933>")

@bot.command(pass_context=True)
async def llamas(ctx):
    await bot.say("<:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933><:HappyLlama:429081444577574933>")
    
@bot.command(pass_context=True)
async def drug(ctx):
    await bot.say("Drugs are Baaaad!")

@bot.command(pass_context=True)
async def coinflip(ctx):
    pick = ['Heads', 'Tails']
    outcome = random.choice(pick)
    await bot.say("The Llamas are flipping the Coin!")
    await asyncio.sleep(1)
    await bot.say("The coin landed on %s!" % (outcome))

@bot.command(pass_context=True)
async def dice(ctx):
    r=random.randint(1,6)
    embed = discord.Embed(title="You rolled a %s" % (r), color=0x00ff00)
    embed.set_thumbnail(url="https://image.prntscr.com/image/zCXDzFN1QzKCrKIjd9n61g.png")
    await bot.say(embed=embed) 

@bot.command(pass_context=True)
async def oof(ctx):
    await bot.say("OOOOOFFFF")

@bot.command(pass_context=True)
async def awake(ctx):
    await bot.say("Yes! I'm awake!") 


@bot.command(pass_context=True)
async def ball(ctx):
    choice = ['It is certain','As I see it, yes','It is decidedly so','Most likely','Without a doubt',' Outlook good','Yes','Yes definitely ','You may rely on it','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again',"Don't count on it",'My reply is no','My sources say no','Outlook not so good','Very doubtful']      
    outcome = random.choice(choice)
    await bot.say(":8ball:|"+outcome)

@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("Howdy!")

@bot.command
async def shutdown(ctx):
    await bot.say("Da Llamas Shutdown down the Bot, Callama!")
    bot.logout()










@bot.command(pass_context = True)
async def clear(ctx, number):
    number = int(number) 
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        await bot.delete_message(x)

@bot.command(pass_context=True)
async def randomllama(ctx):
    await bot.say("Its ARandomLlama! https://image.prntscr.com/image/iY2_RZkFRCSuZDVKPPUaug.jpg")
            
         



bot.run('')
        
       












