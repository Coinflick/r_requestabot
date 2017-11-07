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
            msg = await self.bot.say("Click one of the buttons below to get a role that shows off your favourite group!")
            await self.bot.add_reaction(msg, "<:akb:376005222876839936>")
            await self.bot.add_reaction(msg, "<:ske:376001727410864138>")
            await self.bot.add_reaction(msg, "<:nmb:376005223141081102>")
            await self.bot.add_reaction(msg, "<:hkt:376005223065452578>")
            await self.bot.add_reaction(msg, "<:ngt:376005223078166545>")
            await self.bot.add_reaction(msg, "<:jkt:376005223145144330>")
            await self.bot.add_reaction(msg, "<:stu:376005223233224724>")
            await self.bot.add_reaction(msg, "<:tpe:376005223308853248>")
            await self.bot.add_reaction(msg, "<:mnl:376005223145144321>")
            await self.bot.add_reaction(msg, "<:bnk:376005223052869632>")
            await self.bot.add_reaction(msg, "<:nogi:376400738403745804>")
            await self.bot.add_reaction(msg, "<:keya:376400681160146953>")
            while True:
                res = await self.bot.wait_for_reaction(['\U0001F1E7\U0001F1EA', '\U0001F1F3\U0001F1F1'], message=msg)
                if res.user.id != "369635547116863488":
                    print(res.user.id)
                    await self.bot.say("User: {}, Reaction: {}, Server: {}".format(res.user, res.reaction.emoji, msg.server.id))
                    await self.bot.remove_reaction(msg, res.reaction.emoji, res.user)
                    print(res.reaction.emoji)
                    if res.reaction.emoji == '<:akb:376005222876839936>':
                        if 'AKB' in [x.name for x in res.user.roles]:
                                await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'AKB'))

                    elif res.reaction.emoji == '<:ske:376001727410864138>':
                        if 'SKE' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'SKE'))
                    elif res.reaction.emoji == "<:nmb:376005223141081102>":
                         if 'NMB' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'NMB'))
                    elif res.reaction.emoji == "<:hkt:376005223065452578>":
                        if 'HKT' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'HKT'))
                    elif res.reaction.emoji == "<:ngt:376005223078166545>":
                        if 'NGT' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'NGT'))
                    elif res.reaction.emoji == "<:jkt:376005223145144330>":
                        if 'JKT' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'JKT'))
                    elif res.reaction.emoji == "<:stu:376005223233224724>":
                        if 'STU' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'STU'))
                    elif res.reaction.emoji == "<:tpe:376005223308853248>":
                         if 'TPE' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'TPE'))
                    elif res.reaction.emoji == "<:mnl:376005223145144321>":
                         if 'MNL' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'MNL'))
                    elif res.reaction.emoji == "<:bnk:376005223052869632>":
                         if 'BNK' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'BNK'))
                    elif res.reaction.emoji == "<:nogi:376400738403745804>":
                         if 'NOGI' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'NOGI'))
                    elif res.reaction.emoji == "<:keya:376400681160146953>":
                         if 'KEYA' in [x.name for x in res.user.roles]:
                            await self.bot.send_message(res.user, "You already have that role!")
                        else:
                            await self.bot.add_roles(res.user,
                                             get_role(self.bot.get_server(msg.server.id).roles, 'KEYA'))
                    else:
                        print("huh")

def setup(bot):
bot.add_cog(main_cog(bot))
