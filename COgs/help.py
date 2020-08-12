import discord
from discord.ext import commands
from discord.enums import ActivityType, Status
from types import SimpleNamespace

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        colour = discord.Colour.from_rgb(54, 57, 62)
        embed = discord.Embed(colour = colour, timestamp = ctx.message.created_at)
        embed2 = discord.Embed(colour = colour, timestamp = ctx.message.created_at)
        embed3 = discord.Embed(colour = colour, timestamp = ctx.message.created_at)
        embed4 = discord.Embed(colour = colour, timestamp = ctx.message.created_at)
        embed.set_author(name="General help")
        embed2.set_author(name="Moderation help")
        embed3.set_author(name="Marketplace help")


        embed.add_field(name = "Help", value="Shows this message", inline=False)
        embed.add_field(name = "Ping", value="Gives ping of the bot", inline=False)
        embed.add_field(name = "Hub", value="Gives you link to hub", inline=False)
        embed.add_field(name = "Group ", value="Gives you link to the group", inline=False)
        embed.add_field(name = "Suggest", value="Gives a suggetion", inline=False)
        embed.add_field(name = "Info", value="Gives info about a person", inline=False)
        embed3.add_field(name= "ad" , value = "Adds an advertisement in the advertising channel.", inline=False)
        embed3.add_field(name = "sell" , value = "adds a selling ad in selling channel", inline=False)
        embed3.add_field(name = "hire" , value = "adds a hire ad in hiring channel" , inline=False)
        embed2.add_field(name = "ban" , value = "bans a person", inline=False)
        embed2.add_field(name = "unban" , value = "unbans no need of mention use like Expressingames#2342", inline=False)
        embed2.add_field(name = "announce" , value = "announce something in a channel usage: .announce #announcement yo mama(this is the embed version)", inline=False)
        embed2.add_field(name = "say " , value = "says something", inline=False)
        embed2.add_field(name = "announce 2 " , value = "text announce usage same as announce")
        embed2.add_field(name = "dm" , value = "dms a user", inline=False)
        embed.add_field(name = "mb" , value="membercount" , inline=False)
        embed.add_field(name = 'check' , value="checks if user name is avaiable" , inline=False)
        embed.add_field(name = 'allie' , value="apply for allie" , inline=False)
        embed.set_footer(text=f"all commands have . as prefix")
        embed2.set_footer(text=f"all commands have . as prefix")
        embed3.set_footer(text=f"all commands have . as prefix")

        await ctx.author.send(embed=embed)
        await ctx.author.send(embed=embed2)
        await ctx.author.send(embed=embed3)
        await ctx.send("We have sent you a DM.")
def setup(bot):
    bot.add_cog(Help(bot))
