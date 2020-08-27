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


        embed.add_field(name = ".Help", value="Ahows this message", inline=False)
        embed.add_field(name = ".Ping", value="Gives ping of the bot", inline=False)
        embed.add_field(name = ".Hub", value="Gives you link to hub", inline=False)
        embed.add_field(name = ".Group ", value="Gives you link to the group", inline=False)
        embed.add_field(name = ".Suggest", value="Gives a suggetion", inline=False)
        embed.add_field(name = ".Info", value="Gives info about a person", inline=False)
        embed3.add_field(name= ".Ad" , value = "Adds an advertisement in the advertising channel.", inline=False)
        embed3.add_field(name = ".Sell" , value = "Adds a selling ad in selling channel", inline=False)
        embed3.add_field(name = ".Hire" , value = "Adds a hire ad in hiring channel" , inline=False)
        embed2.add_field(name = ".Ban" , value = "Bans a user", inline=False)
        embed2.add_field(name = ".Unban" , value = "Unbans no need for mentions, use there name and tag e.g. Fantom XR#8288", inline=False)
        embed2.add_field(name = ".Announce" , value = "Announce something in a channel usage: .announce #announcement yo mama(this is the embed version)", inline=False)
        embed2.add_field(name = ".Say " , value = "Says something", inline=False)
        embed2.add_field(name = ".Announce 2 " , value = "Text announce usage same as announce")
        embed2.add_field(name = ".Dm" , value = "Dms a user", inline=False)
        embed.add_field(name = ".Mb" , value="Membercount" , inline=False)
        embed.add_field(name = '.Allie' , value="Apply for allie" , inline=False)
        embed.set_footer(text=f"All commands have . as prefix")
        embed2.set_footer(text=f"All commands have . as prefix")
        embed3.set_footer(text=f"All commands have . as prefix")

        await ctx.author.send(embed=embed)
        await ctx.author.send(embed=embed2)
        await ctx.author.send(embed=embed3)
        await ctx.send("We have sent you a DM.")
def setup(bot):
    bot.add_cog(Help(bot))
