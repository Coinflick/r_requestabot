import discord
from discord.ext import commands
import random

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

def setup(bot):
    bot.add_cog(main_cog(bot))
