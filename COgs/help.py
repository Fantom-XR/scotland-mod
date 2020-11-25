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


        embed.add_field(name = ".help", value="Shows a list of all commands.", inline=False)
        embed.add_field(name = ".ping", value="Test our server speed.", inline=False)
        embed.add_field(name = ".hub", value="Gives a link to our purchase hub.", inline=False)
        embed.add_field(name = ".group ", value="Gives a link to our Roblox Group.", inline=False)
        embed.add_field(name = ".suggest", value=".Suggest [ Suggestion Here ]", inline=False)
        embed.add_field(name = ".info", value=".info [ @User ]", inline=False)
        embed3.add_field(name= ".ad" , value = "Publish an advert to <#724241221395939330>", inline=False)
        embed3.add_field(name = ".hire" , value = "Publish a hiring advert to <#724241277826105374>" , inline=False)
        embed2.add_field(name = ".ban" , value = ".ban [ User - Do not @ ] [ Reason(s) ]", inline=False)
        embed2.add_field(name = ".unban" , value = ".unban [ User - Do not @ ]", inline=False)
        embed2.add_field(name = ".kick" , value = ".kick [ User - Do not @ ] [ Reason(s) ]", inline=False)
        embed2.add_field(name = ".announce" , value = ".announce [ #channel ] [ Message ] - Embedded", inline=False)
        embed2.add_field(name = ".announce2 " , value = ".announce2 [ #channel ] [ Message ] - Text")
        embed2.add_field(name = ".say " , value = ".say [ Message ]", inline=False)
        embed2.add_field(name = ".clear" , value = ".clear [ Number of Messages ]", inline=False)
        embed2.add_field(name = ".dm" , value = ".dm [ @User ] [ Message ]", inline=False)
        embed.add_field(name = ".mb" , value="Member Count" , inline=False)
        embed.add_field(name = '.ally' , value="Ally Application" , inline=False)
        embed.set_footer(text=f"All commands have . as prefix")
        embed2.set_footer(text=f"All commands have . as prefix")
        embed3.set_footer(text=f"All commands have . as prefix")

        await ctx.author.send(embed=embed)
        await ctx.author.send(embed=embed2)
        await ctx.author.send(embed=embed3)
        await ctx.send("Look for a DM from <@681537574593888336>")
def setup(bot):
    bot.add_cog(Help(bot))
