from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
import interactions
from config import TOKEN


help_command = commands.DefaultHelpCommand(
    no_category='Commands')
emojis = {1: ":one:", 2: ":two:", 3: ":three:", 4: ":four:", 5: ":five:", 6: ":six:", 7: ":seven:",
          8: ":eight:", 9: ":nine:", 10: ":keycap_ten:"}
emojis_code = {1: '1️⃣', 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣",
               8: "8️⃣", 9: "9️⃣", 10: "🔟"}
games = ["Centrale", "Les Mines", "L'X", "Démombrer l'infini", "Des maths"]
other_bot_commands = []
bot = interactions.Client(token=TOKEN)


@bot.command(name='hello', description="Say hello.")
async def hello(ctx: interactions.CommandContext):
    await ctx.send(f"Hi there {ctx.author.mention}!")


@bot.command()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound) and not any(command in ctx.message.content for command in other_bot_commands):
        await ctx.send('This command is unknown. Try checking the spelling, or ask the dev to make it into the bot.')
    return error


@bot.event
async def on_member_join(ctx):
    ctx.send("Hello there!")


bot.start()