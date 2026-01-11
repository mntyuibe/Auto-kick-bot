import discord
from discord.app_commands import user_install
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intent = discord.Intents.default()
intent.message_content = True
intent.members = True

bot = commands.Bot(command_prefix='!', intents=intent)

Role_001 = "Test"
Firewall = False

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "ควย" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - Fuck you Nigga")

    await bot.process_commands(message)

@bot.command()

async def fwactive(ctx):
  if ctx.author.id == 752509478242484245:
    global Firewall
    Firewall = True
    await ctx.send("firewall start operation")

@bot.command()

async def fwdeactive(ctx):
   if ctx.author.id == 752509478242484245:
    global Firewall
    Firewall = False
    await ctx.send("firewall ended operation")

@bot.event
async def on_member_join(member):
 if Firewall == True:
    await member.kick(reason="COC_001 Not")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")

@bot.command()
async def ticket(ctx):
    roles = discord.utils.get(ctx.guild.roles, name=Role_001)
    if roles:
        await ctx.author.add_roles(roles)
        await ctx.send(f"{ctx.author.mention} Done")
    else:
        await ctx.send("Sorry no role")
bot.run(token, log_handler=handler, log_level=logging.DEBUG)