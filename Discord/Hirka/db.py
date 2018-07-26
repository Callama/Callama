from discord.ext import commands
import random
import TOKEN
import time
import json
from tinydb import TinyDB, Query
from tinydb.operations import delete,increment
bot = commands.Bot(command_prefix = ";") #Initialise client bot  

uses = {}
class dbs():
    def __init__(self,bot):
        self.bot = bot

       

            


    
            
            
        
        






def setup(bot):
    bot.add_cog(dbs(bot))