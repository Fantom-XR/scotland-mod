import discord
from discord.ext import commands

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
        embed2.set_author(name="Fun help")
        embed3.set_author(name="Moderation help")
        embed4.set_author(name="Marketplace help")


        embed.add_field(name = "Help", value="Shows this message", inline=False)
        embed.add_field(name = "Ping", value="Gives ping of the bot", inline=False)
        embed.add_field(name = "New", value="Opens a ticket (Note: you can also dm ticket bot)", inline=True)
        embed.add_field(name = "Hub", value="Gives you link to hub", inline=False)
        embed.add_field(name = "Group ", value="Gives you link to the group", inline=False)
        embed2.add_field(name = "8ball", value="Its a 8ball you know", inline=False)
        embed.add_field(name = "Suggest", value="Gives a suggetion", inline=False)
        embed.add_field(name = "Info", value="Gives info about a person", inline=False)
        embed4.add_field(name= "ad" , value = "Adds an advertisement in the advertising channel.", inline=False)
        embed4.add_field(name = "sell" , value = "adds a selling ad in selling channel", inline=False)
        embed4.add_field(name = "hire" , value = "adds a hire ad in hiring channel" , inline=False)
        embed3.add_field(name = "ban" , value = "bans a person", inline=False)
        embed3.add_field(name = "unban" , value = "unbans no need of mention use like Expressingames#2342", inline=False)
        embed3.add_field(name = "announce" , value = "announce something in a channel usage: .announce #announcement yo mama(this is the embed version)", inline=False)
        embed3.add_field(name = "say " , value = "says something", inline=False)
        embed3.add_field(name = "announce 2 " , value = "text announce usage same as announce")
        embed3.add_field(name = "dm" , value = "dms a user", inline=False)
        embed2.add_field(name= "choose", value = "chooses in options given by user", inline=False)
        embed2.add_field(name= "roll", value = "rolls a dice", inline=False)
        embed2.add_field(name= "flip", value = "flips a coin", inline=False)
        embed2.add_field(name= "rps", value = "plays rock paper scissors with you haha", inline=False)
        embed2.add_field(name= "roast", value = "roasts someone", inline=False)
        embed2.add_field(name = "emojify" , value = "Emojifies text" , inline=False)
        embed2.add_field(name = "cringe" , value = "cringes a text" , inline=False)
        embed2.add_field(name = "smallcaps" , value = "smallcaps a text" , inline=False)
        embed2.add_field(name = "dadjokes" , value = "gives a dad joke" , inline=False)
        embed2.add_field(name="reverse" , value="reverses the text" , inline=False)
        embed.add_field(name = "mb" , value="membercount" , inline=False)
        

        await ctx.author.send(embed=embed)
        await ctx.author.send(embed=embed2)
        await ctx.author.send(embed=embed3)
        await ctx.author.send(embed=embed4)
        await ctx.send("we dmed you")

def setup(bot):
    bot.add_cog(Help(bot))
