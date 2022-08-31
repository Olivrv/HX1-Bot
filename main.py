import random
import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from config import TOKEN


help_command = commands.DefaultHelpCommand(
    no_category='Commands')
emojis = {1: ":one:", 2: ":two:", 3: ":three:", 4: ":four:", 5: ":five:", 6: ":six:", 7: ":seven:",
          8: ":eight:", 9: ":nine:", 10: ":keycap_ten:"}
emojis_code = {1: '1️⃣', 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣",
               8: "8️⃣", 9: "9️⃣", 10: "🔟"}
games = ["Centrale", "Les Mines", "L'X", "Démombrer l'infini", "Des maths"]
other_bot_commands = []
bot = commands.Bot(command_prefix='!', help_command=help_command, description="")
client = discord.Client()
slash = SlashCommand(bot, sync_commands=True)


@slash.slash(name="hey", description="Good morning")
async def hey(ctx: SlashContext):
    await ctx.send(f"Hello {ctx.author.name}!")


@slash.slash(name="maths", description="Do the maths.",
             options=[create_option(name="formula",
                                    description="What the bot will calculate.",
                                    option_type=3, required=True)])
async def maths(ctx, formula):
    try:
        formulae = "from math import *\n" + 'x = ' + formula
        d = dict()
        exec(formulae, globals(), d)
        x = int(d["x"])
        await ctx.send(f"Solution to {formula} = {x}")
    except (TypeError, SyntaxError, NameError):
        await ctx.send("Error: your formula was not recognised. Use these symbols: *, /, -, +, ., !, sqrt().",
                       hidden=True)


@bot.event
async def on_ready():
    print('Logged in as', end=' ')
    print(bot.user.name, 'also known as ', end='')
    print(bot.user.id)
    print('------')
    game = random.choice(games)
    await bot.change_presence(status=discord.Status.online, activity=Game(name=game))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound) and not any(command in ctx.message.content for command in other_bot_commands):
        await ctx.send('This command is unknown. Try checking the spelling, or ask the dev to make it into the bot.')
    return error


@bot.event
async def on_member_join(ctx):
    ctx.send("Hello there!")


bot.run(TOKEN)
