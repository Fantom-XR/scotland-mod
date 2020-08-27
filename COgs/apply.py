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
        await ctx.author.send("""**RESERVE TECH - ALLY APPLICATION**
        
Reserve Tech Ally Benefits:
- 20% off all products
- Have your group listed in our partner channel
- Ability to post in partner events
- Private Partner Channel

Requirements:
- Your group must free from PR Scandals
- You must have at least 150 group members
- Your reputation must be clean
- When applying, use full punctuation & grammar
- Answer questions in detail and to the best of your ability
- Must be 13+ to apply
- Must have an active community

*Respond to this message to continue, or say "cancel".*
""")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            item = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")

        if item.content == 'cancel':
            return

        else:
            await ctx.author.send("Please state your Discord Username id eg. <@[Your ID here]> and your Roblox Username")
            try:
                price = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("Why do you want to ally with Reserve Tech & how will this partnership benefit us?")
                try:
                    note = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                else:
                    await ctx.author.send("What is your group name and invite link?")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("How long has your group been active for?")
                        try:
                            rating = await self.bot.wait_for('message', check=check, timeout=120)
                        except asyncio.TimeoutError:
                            await ctx.author.send("Timed out")
                        else:
                            await ctx.author.send('Your application has been submit. [ Phase 1/3 ]')

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"New Ally Request")
        embed.add_field(name="Name:", value=price.content, inline=False)
        embed.add_field(name="Reasoning for Ally Request:", value=note.content, inline=False)
        embed.add_field(name="Group Name & Invite:" , value =f"{Image.content}", inline=False)
        embed.add_field(name="Group Active Duration:" , value =f"{rating.content}", inline=False)
        embed.set_footer(text=f"Sent by {ctx.author}")
        channel = self.bot.get_channel(748555001072451654)
        await channel.send(embed=embed)

    @allie.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You have recently requested an ally application. Wait {(int(error.retry_after/0))} minutes to retry.")


def setup(bot):
    bot.add_cog(marketplace(bot))

    
