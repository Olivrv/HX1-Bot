import discord
from discord.ext.commands.errors import CommandNotFound
import interactions
import asyncio
from config import TOKEN


emojis = {1: ":one:", 2: ":two:", 3: ":three:", 4: ":four:", 5: ":five:", 6: ":six:", 7: ":seven:",
          8: ":eight:", 9: ":nine:", 10: ":keycap_ten:"}
emojis_code = {1: '1️⃣', 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣",
               8: "8️⃣", 9: "9️⃣", 10: "🔟"}
games = ["Centrale", "Les Mines", "L'X", "Dénombrer l'infini", "Des maths"]
other_bot_commands = []
bot = interactions.Client(token=TOKEN)


@bot.command(name='hello', description="Say hello.")
async def hello(ctx: interactions.CommandContext):
    await ctx.send(f"Hi there {ctx.author.mention}!")


@bot.command(name="hack", description="hack a player",
             options=[interactions.Option(name="player", type=interactions.OptionType.USER,
                                          required=True, description='player to hack')])
async def hack(ctx: interactions.CommandContext, player):
    msg = await ctx.send(f"Hacking {player}...")
    t = 2
    if ctx.author.id == player.id:
        await msg.edit("Initialising... Wait, no! You can't hack yourself.")
    elif player.id == bot.me.id:
        await msg.edit(f"Initialising... Breached {player}... Hold on a minute... No!")
    else:
        await msg.edit(f"Launching hacking protocols against {player}...")
        await asyncio.sleep(t)
        await msg.edit(content="Breaching firewalls...")
        await asyncio.sleep(t)
        await msg.edit(content="Breaking developers mind...")
        await asyncio.sleep(t)
        await msg.edit(content=f"Looking for {player}'s private folders...")
        await asyncio.sleep(t)
        await msg.edit(content="Sharing them on the internet...")
        await asyncio.sleep(t)
        await msg.edit(content=f"Looking for {player}'s \"Homework\" folder...")
        await asyncio.sleep(t)
        await msg.edit(content=f"Replacing all content with cute kitten images...")
        await asyncio.sleep(t)
        await msg.edit(content="Removing all traces...")
        await asyncio.sleep(t)
        await msg.edit(content=f"Successfully hacked {player}.")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound) and not any(command in ctx.message.content for command in other_bot_commands):
        await ctx.send('This command is unknown. Try checking the spelling, or ask the dev to make it into the bot.')
    return error


@bot.event
async def on_ready():
    print(f"Logged in as {bot.me.name}")


@bot.event
async def on_member_join(ctx):
    ctx.send("Hello there!")


bot.start()
