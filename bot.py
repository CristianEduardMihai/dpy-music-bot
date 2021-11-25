"""
Original code: https://gist.github.com/vbe0201/ade9b80f2d3b64643d854938d40a0a2d

Requirements:
    Python 3.5+
    pip install -U discord.py pynacl youtube-dl

Os requirements:
    On windows:
        `ffmpeg.exe` in your parent directory(already there)
    On linux:
    $ sudo apt update
    $ sudo apt -y install ffmpeg
"""

import discord
from discord.ext import commands
from config import *



bot = commands.Bot(
    command_prefix=bot_prefix, 
    case_insensitive=True, 
    activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=f"{bot_prefix}help"
    )
)

bot.load_extension("cogs.music")

    
@bot.event
async def on_ready():
    print('THE BOT IS READY')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, (commands.MissingPermissions,
              commands.MissingAnyRole, commands.MissingRole)):
        await ctx.send("Missing Permission", delete_after=2.0)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing Required Argument", delete_after=2.0)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Command on cooldown, try again in {:.2f}s.".format(error.retry_after), delete_after=1.0)
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        raise error

bot.run(bot_token)
