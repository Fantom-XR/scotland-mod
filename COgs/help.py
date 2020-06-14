import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        colour = discord.Colour.from_rgb(54, 57, 62)
        embed = discord.Embed(colour = colour, timestamp = ctx.message.created_at)

        embed.add_field(name = "Help", value="Shows this message", inline=False)
        embed.add_field(name = "Ping", value="Gives ping of the bot", inline=False)
        embed.add_field(name = "New", value="Opnes a ticket (Note: you can also dm ticket bot", inline=True)
        embed.add_field(name = "Hub", value="Gives you link to hub", inline=False)
        embed.add_field(name = "Group ", value="Gives you link to the group", inline=False)
        embed.add_field(name = "8ball", value="Its a 8ball you know", inline=False)
        embed.add_field(name = "Suggest", value="Gives a suggetion", inline=False)
        embed.add_field(name = "Info", value="Gives info about a person", inline=False)
        await ctx.author.send(embed=embed)
        await ctx.send("we dmed you")

def setup(bot):
    bot.add_cog(Help(bot))