import discord
from discord.ext import commands
import asyncio

def get_role(server_roles, target_name):
   for each in server_roles:
      if each.name == target_name:
         return each
   return None

# n  \U0001F1F3\U0001F1F1
# b  \U0001F1E7\U0001F1EA

class main_cog():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roles(self):
            msg = await self.bot.say("Reageer met \U0001F1E7\U0001F1EA om de 'België' rank te ontvangen, of \U0001F1F3\U0001F1F1 om de 'Nederland' rank te ontvangen. **Je mag ALLEEN jou gewilde emoji aanklikken als 2 seconden zijn gepas")
            await self.bot.add_reaction(msg, "\U0001F1E7\U0001F1EA")
            await self.bot.add_reaction(msg, "\U0001F1F3\U0001F1F1")
            while True:
                res = await self.bot.wait_for_reaction(['\U0001F1E7\U0001F1EA', '\U0001F1F3\U0001F1F1'], message=msg)
                if res.user.id != "369635547116863488":
                    print(res.user.id)
                    await self.bot.say("User: {}, Reaction: {}, Server: {}".format(res.user, res.reaction.emoji, msg.server.id))
                    await self.bot.remove_reaction(msg, res.reaction.emoji, res.user)
                    print(res.reaction.emoji)
                    if res.reaction.emoji == '\U0001F1E7\U0001F1EA':
                        if 'België' in [x.name for x in res.user.roles]:
                                await self.bot.send_message(res.user, "FOUT: Jij hebt die rank al!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'België'))

                    elif res.reaction.emoji == '\U0001F1F3\U0001F1F1':
                        if 'Nederland' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "FOUT: Jij hebt die rank al!")
                        else:
                            await self.bot.add_roles(res.user,
                                                 get_role(self.bot.get_server(msg.server.id).roles, 'Nederland'))
                    else:
                        print("huh")

def setup(bot):
    bot.add_cog(main_cog(bot))
