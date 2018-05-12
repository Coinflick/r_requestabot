import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='`')
extensions = ['main_cog']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
print('------')

@bot.command()
async def hello():
    await bot.say('hello')

for extension in extensions:
    bot.load_extension(extension)

bot.run("")
