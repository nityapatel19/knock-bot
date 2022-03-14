import os
import datetime

import dotenv
import discord
from discord.ext.commands import Bot, Context

from jokebook import *

dotenv.load_dotenv()

with open('config.json') as f:
    config = json.load(f)

LOG_CHANNEL = config['log_channel']


bot = Bot(command_prefix='$', self_bot=False, case_insensitive=True)


@bot.event
async def on_ready():
    await bot.get_channel(LOG_CHANNEL).send(f"`{datetime.datetime.now()}`\nMe: Knock Knock!\nYou: Who's there?\nMe: "
                                            f"KnockBot.\nYou: KnockBot who?\nMe: KnockBot, the comedy god!")


@bot.command(
    aliases=['hi', 'hey', 'diachronic', 'hola', 'ola', 'salut', 'hallo', 'ciao', 'namaste', 'annyeonghaseyo', 'salve',
             'nihao', 'privet'])
async def hello(ctx: Context):
    await ctx.reply(content=f"Hello {ctx.author.mention} :wave:")


@bot.command()
async def knockknock(ctx: Context):
    joke = get_joke()
    msg = ctx.author.mention + '\n'
    msg += '\n'.join(joke['content']) + '\n :joy: :joy:'
    await ctx.reply(content=msg)
    # await ctx.reply(content=f"{ctx.author.mention}\n{'\n'.join(joke['content'])}\n:joy: :joy:")


@bot.command()
async def knock(ctx: Context):
    ...

if __name__ == '__main__':
    # bot.run(os.getenv('DISCORD_TOKEN'))
    mark_all_unread()