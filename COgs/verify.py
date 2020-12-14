import requests
import emoji
import discord
from discord.ext import commands
import asyncio
import random


available_words = ["apple", "orange", "pear", "boat", "ship", "car", "plane", "train", "turtle", "cow", "frog", "sheep"] # Obstain from the number's 6 & 9 due to Roblox's filter
tempStorage = [] # Holds Random Keys
temp_passphrase = ' '.join((random.choice(available_words) for i in range(8)))

class veirfy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
   @commands.cooldown(1,3600,BucketType.member)
    async def veirfy(self, ctx):
        await ctx.send('check your dm')
        await ctx.author.send("wot your username?")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            name = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.author.send(f"please place this in yout status {temp_passphrase}  and say done when done")
            try:
                item = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            test = {'usernames': name.content,
                    'excludeBannedUsers': False,}
            test = f'{test}'
            api = requests.post('https://users.roblox.com/v1/usernames/users' , data =test, headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
            if item.content == 'done' and emoji.emojize(api.json()['description']) == temp_passphrase:            
                    #await ctx.author.edit(nick=api.json()["data"][0]["displayName"])
                    await ctx.send(api.json()["data"][0]["displayName"])

            else:
                await ctx.author.send("some error")
def setup(bot):
    bot.add_cog(veirfy(bot))




api = requests.get(f'https://users.roblox.com/v1/users/{user}')


print(emoji.emojize(api.json()['description']))
