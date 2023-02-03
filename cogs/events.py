import asyncio
import random
from datetime import datetime
from datetime import timedelta
import discord
from discord.ext import commands
from discord import (
    ComponentInteraction,ModalSubmitInteraction,Modal,TextInput,Button,ButtonStyle,SlashCommandOption as Option,ApplicationCommandInteraction as APPCI)
class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_user = None

def setup(bot):
    bot.add_cog(cmds(bot))