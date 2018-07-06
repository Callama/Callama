import discord
from discord.ext import commands
import requests
import inspect
import random
import os


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
    
    @bot.command(pass_context=True)
    async def insult(self,ctx,person : str = None):
            answers = ["If laughter is the best medicine, your face must be curing the world.", "It's better to let someone think you are an idiot than to open your mouth and prove it.", "If I had a face like yours, I'd sue my parents.", "You're so ugly, when your mom dropped you off at school she got a fine for littering.", "If I wanted to kill myself I'd climb your ego and jump down to your IQ.", "Brains aren't everything. In your case they're nothing.", "Are you always this stupid or is today a special occasion?", "Don't you have a terribly empty feeling - in your skull?", "How did you get here? Did someone leave your cage open?", "I'd like to see things from your point of view but I can't seem to get my head that far up my ass.", "Have you been shopping lately? They're selling lives, you should go get one.", "The last time I saw something like you, I flushed it.", "If ugliness was measured in bricks, you would be the Great Wall of China.", "You want an insult? Look in the mirror!", "Your life is more insulting than anything I have to say.", "Did a thought cross your mind? It must have been a long and lonely journey...", "You'd better hide; the garbage man is coming.", "Roses are red, violets are blue, I have five fingers, the middle one's for you.", "I have a text file bigger than your brain in my database. It's 0KB in size.", "You're old enough to remember when emojis were called 'hieroglyphics.'", "I don't engage in mental combat with the unarmed.", "Is your arse jealous of the amount of crap that comes out of your mouth?", "Your face looks like it caught fire and someone tried to put it out with a fork.", "Hey, you have something on your third chin.", "I thought a little girl from Kansas dropped a house on you…", "I'm jealous of people that don't know you.", "You bring everyone a lot of joy, when you leave the room.", "If you are going to be two faced, at least make one of them pretty.", "If you're going to be a smartarse, first you have to be smart. Otherwise you're just an arse.", "Somewhere out there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology.", "I don't exactly hate you, but if you were on fire and I had water, I'd drink it.", "If you were on TV, I would change the channel.", "You have Diarrhea of the mouth; constipation of the ideas.", "If ugly were a crime, you'd get a life sentence.", "There is no vaccine against stupidity."]
            outcome = random.choice(answers)
            await self.bot.say(outcome)
    @bot.command(pass_context=True,no_pm=True, hidden=True)
    async def hug(self,ctx, user : discord.Member, intensity : int=1):
        """Because everyone likes hugs
        Up to 10 intensity levels."""
        name = '*{}*'.format(user.display_name)
        if intensity <= 0:
            msg = "(っ˘̩╭╮˘̩)っ" + name
        elif intensity <= 3:
            msg = "(っ´▽｀)っ" + name
        elif intensity <= 6:
            msg = "╰(*´︶`*)╯" + name
        elif intensity <= 9:
            msg = "(つ≧▽≦)つ" + name
        elif intensity >= 10:
            msg = "(づ￣ ³￣)づ{} ⊂(´・ω・｀⊂)".format(name)
        await self.bot.say(msg)

    

            
            
            
        
            

    

def setup(bot):
    bot.add_cog(fun(bot))