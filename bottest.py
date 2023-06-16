import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} としてログインしました。')

@bot.command()
async def echo(ctx, *, message=None):
    message = message or "エコーのメッセージを指定してください。"
    await ctx.send(message)

bot.run('ODA5Mzc3ODgzNDgzMDEzMTQx.GZV4iK.uOn77XyNedCsTGj4kFW2UOETTMUrafL6NbirTk')
