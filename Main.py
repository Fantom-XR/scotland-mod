import discord
from discord.ext import commands, tasks
from discord.ext.commands.cooldowns import BucketType
import random

bot = commands.Bot(command_prefix=commands.when_mentioned_or(':'))
bot.remove_command("help")


@bot.event
async def on_ready():
    print("signed as Scotland Moderation \n prefix is :")
    await bot.change_presence(activity=discord.Game(name="Stay Home | Protect the NHS | Save Lives"))

@bot.command()
async def ping(ctx):
    """|| Tells the bot's latency """
    await ctx.send(f"{round(bot.latency * 1000)} ms")

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

"""@bot.command()
@commands.guild_only()
@commands.has_guild_permissions(administrator = True)
async def dm(ctx, member: discord.Member, * , text=None) :
    await member.send(f"{text}")"""
    

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


'''@bot.command(name="8ball")
async def _ball(ctx):
    """|| its a 8ball!"""
    await ctx.send(random.choice(["yes", "no", "maybe", "ask person above you", "why asking me you bully", "who knows?", "im busy talk later", "no u",]))'''


@tasks.loop(seconds = 600)
async def member():
    name1 = (f"Member Count : {member.guild.member_count}")
    chan = member.guild.get_channel(806253474265563166)
    await chan.edit(name=name1)

@bot.command()
async def mb(ctx):
    await ctx.send(f"there are {ctx.guild.member_count} members in the server!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    brooklyn_99_quotes = [
        'Nah',
        'No u ',
        'well thats not the truth',
        'well whats the prob boomer?',
    ]

    if message.content in ('This bot sucks','this bot sucks', 'Thus bot is bad', 'scotland bot needs work', 'ew this bot', 'scotland sucks'):
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    await bot.process_commands(message)

bot.load_extension("COgs.help")
#bot.load_extension("COgs.report")
bot.load_extension("COgs.moderaion")
bot.load_extension("COgs.apply")
bot.load_extension("COgs.sfrs")
bot.load_extension("COgs.nhs")
#bot.load_extension("COgs.verify")

bot.run("ODE0ODU3MTEyNDU4MTAwNzM2.YDj80g.uR2a6MLoGwMmeLmh_gq972ztglk")
