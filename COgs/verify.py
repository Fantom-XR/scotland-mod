import requests
import emoji
import discord
from discord.ext import commands
import asyncio
import random


#Words = [':smile:', ':point_down:', ':cloud_snow:', ':second_place:',':cookie:', ':cloud:']
#random.shuffle(Words)
#print(Words)

class veirfy(commands.Cog):

    def __init__(self, bot):
        self.Words = [':smile:', ':point_down:', ':cloud_snow:', ':second_place:',':cookie:', ':cloud:']
        self.bot = bot
    
    #Words = [':smile:', ':point_down:', ':cloud_snow:', ':second_place:',':cookie:', ':cloud:']
    #random.shuffle(Words)
    #print(Words)

    @commands.command()
#    @commands.cooldown(1,3600,BucketType.member)
    async def veirfy(self, ctx):
        random.shuffle(self.Words)

        await ctx.send('check your dm')
        await ctx.author.send("wot your username?")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            name = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.author.send(f"please place this in yout status {self.Words} and say done when done")
            try:
                item = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            test = f'''{
                        "usernames": [
                            "{name.content}"
                        ],
                        "excludeBannedUsers": false
                        }'''         
            api = requests.post('https://users.roblox.com/v1/usernames/users' , data =test, headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
            if item.content == 'done' and emoji.emojize(api.json()['description']) == Words:            
                    await ctx.author.edit(nick=api.json()["data"][0]["displayName"])

            else:
                await ctx.author.send("some error")
def setup(bot):
    bot.add_cog(veirfy(bot))




#api = requests.get(f'https://users.roblox.com/v1/users/{user}')


#print(emoji.emojize(api.json()['description']))