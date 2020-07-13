import discord
from discord.ext import commands
import robloxpy

bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'))



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def check(self, ctx, name):
        Divine = robloxpy.DoesNameExist(name)
        await ctx.send(Divine)
    
    



bot.run("NjgxNTM3NTc0NTkzODg4MzM2.XucL2A.Q0wkpqwo8cZW7vT-1GDdBx5HFIM")