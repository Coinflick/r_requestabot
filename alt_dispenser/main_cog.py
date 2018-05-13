import discord
from discord.ext import commands
import random
from pathlib import Path
import os

bronze_limit = 1
silver_limit = 2
diamond_limit = 3


def addUser(id):
    my_file = Path("users.txt")
    if not my_file.is_file():
        f = open("users.txt", "w+")
        f.close()
    else:
        with open("users.txt", "w") as f:
            f.write("{}:{}\n".format(id,"1"))
            return False 
    with open("users.txt").read() as in_:
        in_ = in_.rstrip("\n")
        accs = dict(item.split(":") for item in in_.split("\n"))
        if id in accs:
            accs[id] = str(int(accs[id]) + 1)
        else:
            accs[id] = 1
    with open("users.txt", "w") as out:
        for i in list(accs.keys()):
            out.write(i + ":" + accs[i] + "\n")


def check(role, id):
    my_file = Path("users.txt")
    if not my_file.is_file() or os.stat("users.txt").st_size == 0:
        return False
    f = open("users.txt").read()
    f = f.rstrip("\n")
    accs = dict(item.split(":") for item in f.split("\n"))
    if id in accs:
        if role == "bronze":
            limit = bronze_limit
        elif role == "silver":
            limit = silver_limit
        elif role == "diamond":
            limit = diamond_limit 
        if int(accs[id]) >= limit:
            return True
        else:
            return False

def process(file):
    f = open(file).read()
    f = f.rstrip("\n")
    accs = dict(item.split(":") for item in f.split("\n"))
    # Choose random account
    account_key = random.choice(list(accs.keys()))
    account = accs[account_key]
    # Delete it
    accs.pop(account_key, None)
    f = open(file, "w")
    # Restructure dictoinary into file
    for i in list(accs.keys()):
        f.write(i + ":" + accs[i] + "\n")
    f.close()
    return account_key + ":" + account

def get_acc(role, type):
    if role == "bronze":
        if type == "minecraft":
            return process("minecraft_bronze.txt")
        elif type == "spotify":
            return process("spotify_bronze.txt")
    elif role == "silver":
        if type == "minecraft":
            return process("minecraft_silver.txt")
        elif type == "spotify":
            return process("spotify_silver.txt")
    elif role == "diamond":
        if type == "minecraft":
            return process("minecraft_diamond.txt")
        elif type == "spotify":
            return process("spotify_diamond.txt")

class main_cog():
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def get(self, ctx, type):
        msg = await self.bot.say("Please wait...")
        if 'bronze' in [x.name for x in ctx.message.author.roles]:
            if check("bronze", ctx.message.author.id) == True:
                self.bot.say("You have used the max alts for today " + ctx.message.author.mention)
                return False
        elif 'silver' in [x.name for x in ctx.message.author.roles]:
            if check("silver", ctx.message.author.id) == True:
                self.bot.say("You have used the max alts for today " + ctx.message.author.mention)
                return False
        elif 'diamond' in [x.name for x in ctx.message.author.roles]:
            if check("diamond", ctx.message.author.id) == True:
                self.bot.say("You have used the max alts for today " + ctx.message.author.mention)
                return False
        try:
            pm = await self.bot.send_message(ctx.message.author, "Please wait, this message will update shortly with the information.")
        except:
            await self.bot.edit_message(msg, "I couldn't PM you, maybe your privacy settings on this server restrict that? " + ctx.message.author.mention)
            return False
        if 'bronze' in [x.name for x in ctx.message.author.roles]:
            await self.bot.edit_message(pm, get_acc("bronze",type))
        elif 'silver' in [x.name for x in ctx.message.author.roles]:
            await self.bot.edit_message(pm, get_acc("silver",type))
        elif 'diamond' in [x.name for x in ctx.message.author.roles]:
            await self.bot.edit_message(pm, get_acc("diamond",type))
        addUser(ctx.message.author.id)
        print("user added")

def setup(bot):
    bot.add_cog(main_cog(bot))
