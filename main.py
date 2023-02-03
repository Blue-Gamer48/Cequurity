import logging
from logging.handlers import HTTPHandler
import sys, traceback
import platform
import os
import json
import aiohttp
import time
from pathlib import Path
from _datetime import datetime
import asyncio
from asyncio import sleep
from discord.ext import commands
import discord

print(__file__)
import config
from config import (
    DISCORD_TOKEN,
)

def run_check():
    if sys.version_info < (3, 10):
        exit(f"Du musst dieses Script mit Python 3.10 oder höher ausführen!")
    return

time1 = datetime.now()
time2 = time1.strftime("%m-%d-%Y-%H-%M-%S")
log = logging.getLogger('BOT-MAIN')
intents = discord.Intents.all()
user="Saturnbot"
bot = commands.Bot(command_prefix="c.",intents=intents, sync_commands=True,delete_not_existing_commands=True)
time1 = datetime.now()
time2 = time1.strftime("%m-%d-%Y-%H-%M-%S")



if __name__ == '__main__':
    print('Starting bot...')
    print("\n----------------------------------------------------------------\n")
    print(f'Der Bot mit dem Namen "{user}" wurde erfolgreich gestartet!\n')
    print(f"Discord.py Version: {discord.__version__}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Operating System: {platform.system()} {platform.release()} ({os.name})")
    print("\n----------------------------------------------------------------\n")
    logging.info("\n----------------------------------------------------------------\n")
    logging.info('Saturnbot Logs')
    logging.info("------")
    logging.info(f'Der Bot mit dem Namen {user} wurde erfolgreich gestartet!\n')
    logging.info(f"Discord.py Version: {discord.__version__}")
    logging.info(f"Python Version: {platform.python_version()}")
    logging.info(f"Operating System: {platform.system()} {platform.release()} ({os.name})")
    logging.info("\n----------------------------------------------------------------\n")
    print('Loading cogs...')
    cogs = [file.stem for file in Path('cogs').glob('**/*.py') if not file.name.startswith('__')]
    print(f'Loading {len(cogs)} cogs...')
    for cog in cogs:
        bot.load_extension(f'cogs.{cog}')
        print(f'Loaded cog {cog}')
    bot.run(DISCORD_TOKEN)