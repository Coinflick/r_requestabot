import discord
from discord.ext import commands
import random

class main_cog():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def code(self, ctx):
        self.bot.send_message(ctx.message.author, str(random.randint(1000, 9000)))
        
