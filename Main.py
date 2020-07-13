import discord
from discord.ext import commands, tasks
from discord.ext.commands.cooldowns import BucketType
import random

bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'))
bot.remove_command("help")


@bot.event
async def on_ready():
    print("signed as reserve bot \n prefix is .")
    await bot.change_presence(activity=discord.Game(name=".help"))

@bot.command()
async def ping(ctx):
    """|| Tells the bot's latency """
    await ctx.send(f"{round(bot.latency * 1000)} ms")

@bot.event
async def on_member_join(member):
    chan1 = member.guild.get_channel(724211449760710696)
    await chan1.send(f"welcone {member.mention}, there are {member.guild.member_count} members in the server ! ")

@bot.event
async def on_member_remove(member):
    chan = member.guild.get_channel(724211449760710696)
    await chan.send(f"{member.mention} decided to leave Reserve Tech :( , there are {member.guild.member_count} members in the server now")

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
@commands.cooldown(1,3600,BucketType.member)
async def suggest(ctx, *, message=None):
    """
    || Gives a suggestion in suggestion channel
    """
    if not message:
        await ctx.send("Please Introduce a suggestion :/")
        return
 
    channel = bot.get_channel(724241618516836383)
    message = message
 
    embed = discord.Embed(timestamp=ctx.message.created_at)

    embed.set_author(name='New Suggestion!')

    embed.add_field(name='Suggestion By:', value=ctx.author.mention)
    embed.add_field(name='Suggestion:', value=message)
    
    

    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} your suggestion has been send!")
    await channel.send(embed =embed)


@bot.command()
async def hub(ctx):
    """|| gives you link to the hub!"""
    await ctx.send("https://www.roblox.com/games/5199442577/Hub")

#link to group

@bot.command()
async def group(ctx):
    """|| Gives you link the the group!"""
    await ctx.send("https://web.roblox.com/groups/5648445/Reserve-Tech#!/aboutemoji_2")


'''@bot.command(name="8ball")
async def _ball(ctx):
    """|| its a 8ball!"""
    await ctx.send(random.choice(["yes", "no", "maybe", "ask person above you", "why asking me you bully", "who knows?", "im busy talk later", "no u",]))'''


@bot.command()
@commands.guild_only()
@commands.cooldown(1,3600,BucketType.member)
async def new(ctx,*, reason=None):
    """|| Makes a ticket (Note:you can also dm ticket bot!) """
    #role = ctx.guild.get_role(704326484558348379)
    #role.send(f"{ctx.author.mention} has made a ticket for the reason {reason} please check it if not yet")
    overwrites = {
    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
    ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
    ctx.guild.get_role(715460330716790795): discord.PermissionOverwrite(read_messages=True),
    ctx.author : discord.PermissionOverwrite(send_messages=True,read_messages=True)}
    cat = ctx.guild.get_channel(727879237607882836)
    car = (f"{ctx.author}'s ticket")
    channel = await cat.create_text_channel(name=car,overwrites=overwrites, reason=reason, option=None,topic=reason)
    await channel.send(f"hey, {ctx.author.mention} this is your ticket please wait atleast 8 hours till someone replys and do not ping if no one has seen the ticket yet")

@tasks.loop(seconds = 600)
async def member():
    name1 = (f"Member Count : {member.guild.member_count}")
    chan = member.guild.get_channel(726053858643673198)
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

    if message.content in ('Reserve bot sucks','this bot sucks', 'reserve bot is bad', 'reserve bot needs work', 'ew this bot', 'reserve sucks'):
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    await bot.process_commands(message)

@suggest.error
async def suggest_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Hey! you need to wait {(int(error.retry_after/60))} mins before using it again!")

@new.error
async def suggest_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Hey! you need to wait {(int(error.retry_after/60))} mins before using it again! ")

bot.load_extension("COgs.help")
bot.load_extension("COgs.sell")
bot.load_extension("COgs.fun")
bot.load_extension("COgs.moderaion")
bot.load_extension("COgs.apply")
#bot.load_extension("COgs.verify")

bot.run("NjgxNTM3NTc0NTkzODg4MzM2.XucL2A.Q0wkpqwo8cZW7vT-1GDdBx5HFIM")