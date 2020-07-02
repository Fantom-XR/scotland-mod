import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def allie(self, ctx):
        await ctx.send('check your dm')
        await ctx.author.send("""RESERVE TECH - ALLIE APPLICATION
What are the benefits of becoming our allie?
- Able to announce events in our events channel
- Have your name listed in our partners channel
- Occasional shout-outs
- And more!
Requirements
- You must not be involved in any drama
- Must have atleat 100 members in discord
- You must have a decent or better reputation
- Use full grammar and punctuation
- Answer questions in detail and to the best of your ability
- Must have 50+ members 
Good luck!

**IF YOU DONT MEET REQUIREMENTS SAY cancle OR LEAVE JUST LEAVE WITHOUT SAYING ANYTHING YOU CAN ALSO SAY CANCEL ANYTIME""")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            item = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")

        if item.content == 'cancel':
            return

        else:
            await ctx.author.send("What is your Discord Username and tag and also mention your roblox name.")
            try:
                price = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            if price.content == 'cancel':
                return
            else:
                await ctx.author.send("Why do you want to allie with us? how will reserve tech be benifitted by forming a alliance with you?")
                try:
                    note = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                if note.content == 'cancel':
                    return
                else:
                    await ctx.author.send("Describe your group in detail")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        await ctx.author.send("Timed out")
                    if Image.content == 'cancel':
                        return
                    else:
                        await ctx.author.send("On a scale of 1 to 10, how good is your group? (Your own opinion, be honest)")
                        try:
                            rating = await self.bot.wait_for('message', check=check, timeout=120)
                        except asyncio.TimeoutError:
                            await ctx.author.send("Timed out")
                        if rating.content == 'cancel':
                            return
                        else:
                            await ctx.author.send('DONE!')

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"allie form by {ctx.author.mention}")
        embed.add_field(name="name", value=price.content)
        embed.add_field(name="why allie", value=note.content)
        embed.add_field(name="detail" , value =f"{Image.content}")
        embed.add_field(name="own opinion" , value =f"{rating.content}")
        embed.set_footer(text=f"Send by {ctx.author}")
        channel = self.bot.get_channel(725665272622481448)
        await channel.send(embed=embed)

    @allie.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Hey! you need to wait {(int(error.retry_after/60))} mins before using it again!")


def setup(bot):
    bot.add_cog(marketplace(bot))

    