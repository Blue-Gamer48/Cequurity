import json
import os
import discord
from discord.ext import commands
from discord.utils import get
JSON_FILE = str(os.path.dirname(os.path.realpath(__file__))) + '\data.json'
class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_user = None


    @commands.Cog.listener()
    async def on_ready(self):
        """ Runs once the bot has established a connection with Discord """
        print(f'{self.bot.user.name} has connected to Discord')

        # check if bot has connected to guilds
        if len(self.bot.guilds) > 0:
            print('connected to the following guilds:')

            # list guilds
            for guild in self.bot.guilds:
                # display guild name, id and member count
                print(f'* {guild.name}#{guild.id}, member count: {len(guild.members)}')
                 #update the member count


def get_guild_member_count(guild):
    """ returns the member count of a guild """
    return len(guild.members)

def get_guild_member_count_channel_id(guild):
    """ returns the channel id for the channel that should display the member count """
    with open(JSON_FILE) as json_file:
        # open JSON file
        data = json.load(json_file)
        for data_guild in data['guilds']:
            if int(data_guild['id']) == guild.id:
                return data_guild['channel_id']
            return None
def get_guild_member_count_suffix(guild):
    with open(JSON_FILE) as json_file:
        data = json.load(json_file)
        for data_guild in data['guilds']:
            if int(data_guild['id']) == guild.id:
                return data_guild['suffix']

            return None
def setup(bot):
    bot.add_cog(cmds(bot))