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



bot = commands.Bot(command_prefix=bot_prefix, case_insensitive=True)


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"))
    bot.load_extension("cogs.music")
    print('THE BOT IS READY')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Missing Permission", delete_after=2.0)
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send("Missing Permission", delete_after=2.0)
    elif isinstance(error, commands.MissingRole):
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
