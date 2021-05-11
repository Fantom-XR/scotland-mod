import discord
from discord.ext import commands, tasks
from discord.ext.commands.cooldowns import BucketType
from dotenv import load_dotenv
import os
import random
import aiofiles
import keep_alive

load_dotenv()  # Load environment variables from .env file.


bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'), case_insensitive=True, intents=discord.Intents.all())
bot.remove_command("help")
bot.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="with Tyler 🙈"))

@bot.event
async def on_ready():
    for guild in bot.guilds:
        bot.warnings[guild.id] = {}
        
        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    bot.warnings[guild.id][member_id][0] += 1
                    bot.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    bot.warnings[guild.id][member_id] = [1, [(admin_id, reason)]] 
    
    print(bot.user.name + " is ready.")

@bot.event
async def on_guild_join(guild):
    bot.warnings[guild.id] = {}

@bot.command()
@commands.has_permissions(manage_messages = True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
        
    if reason is None:
        return await ctx.send("Please provide a reason for warning this user.")

    try:
        first_warning = False
        bot.warnings[ctx.guild.id][member.id][0] += 1
        bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = bot.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")

@bot.command()
@commands.has_permissions(manage_messages = True)
async def warnings(ctx, member: discord.Member=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
    
    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in bot.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError: # no warnings
        await ctx.send("This user has no warnings.")
    
@bot.command()
async def ping(ctx):
    """|| Tells the bot's latency """
    await ctx.send(f"{round(bot.latency * 1000)} ms")

@bot.command()
@commands.has_guild_permissions(administrator = True)
async def idle(ctx, * , text=None):
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name=f"{text}"))

@bot.command()
@commands.has_guild_permissions(administrator = True)
async def dnd(ctx, * , text=None):
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name=f"{text}"))

@bot.command()
@commands.has_guild_permissions(administrator = True)
async def online(ctx, * , text=None):
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=f"{text}"))

    
@bot.event
async def on_member_join(member):
    chan1 = member.guild.get_channel(788125714859819098)
    await chan1.send(f"**🚶 Member Left:** {member.mention}, There are now {member.guild.member_count} members.")

@bot.event
async def on_member_remove(member):
    chan = member.guild.get_channel(788125714859819098)
    await chan.send(f"**🚶 Member Left:** {member.mention}, There are now {member.guild.member_count} members.")

@bot.command()
@commands.guild_only()
async def info(ctx, *, member: discord.Member):
    """|| Tells you some info about the member."""
    fmt = '{0} joined on {0.joined_at} and has {1} roles.'
    await ctx.send(fmt.format(member, len(member.roles)))     

@bot.command()
@commands.guild_only()
async def suggest(ctx, *, message=None):
    """
    || Gives a suggestion in suggestion channel
    """
    if not message:
        await ctx.send("Please Introduce a suggestion.")
        return
 
    channel = bot.get_channel(788131736792989726)
    message = message
 
    embed = discord.Embed(timestamp=ctx.message.created_at)

    embed.set_author(name='New Suggestion!')

    embed.add_field(name='Suggestion By:', value=ctx.author.mention)
    embed.add_field(name='Suggestion:', value=message)
   
    
    

    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} your suggestion has been sent! Other users can now see your suggestion, if you would like your suggestion removed please contact a admin.")
    await channel.send(embed =embed)
 
#link to group

@bot.command()
async def group(ctx):
    """|| Gives you link the the group!"""
    await ctx.send("https://www.roblox.com/groups/4170430/Scotland#!/about")

@tasks.loop(seconds = 600)
async def member():
    name1 = (f"Member Count : {member.guild.member_count}")
    chan = member.guild.get_channel(794317984633323532)
    await chan.edit(name=name1)

@bot.command()
async def mb(ctx):
    await ctx.send(f"there are {ctx.guild.member_count} members in the server!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    brooklyn_99_quotes = [
        '<@450260788981137408> is an idiot',
    ]

    if message.content in ('This bot sucks','this bot sucks', 'Thus bot is bad', 'scotland bot needs work', 'ew this bot', 'scotland sucks', 'ethan'):
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    await bot.process_commands(message)

bot.load_extension("COgs.help")
#bot.load_extension("COgs.report")
bot.load_extension("COgs.moderaion")
bot.load_extension("COgs.apply")
bot.load_extension("COgs.sfrs")
bot.load_extension("COgs.nhs")
bot.load_extension("COgs.psoscommands")

bot.run(os.getenv("DISCORDTOKEN"))
