import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def ally(self, ctx):
        await ctx.send('Check for a DM by <@788510771503693854>')
        await ctx.author.send("""**Avenir - STAFF APPLICATION**
        
Avenir Staff Benefits:
- 20% off of products, don't just apply because of this please apply because you think you suit the job.

Requirements:
- Your reputation must be clean.
- When applying, use full punctuation & grammar.
- Answer questions in detail and to the best of your ability
- Must be 13+ to apply
- Must be active

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
            await ctx.author.send("Please state Roblox Username")
            try:
                name = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("Why do you want to become a member of staff at Avenir?")
                try:
                    reason = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                else:
                    await ctx.author.send("How could you benefit Avenir if you became a staff member?")
                    try:
                        benefit = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("How active are you?")
                        try:
                            rating = await self.bot.wait_for('message', check=check, timeout=120)
                        except asyncio.TimeoutError:
                            await ctx.author.send("Timed out")
                        else:
                            
                    await ctx.author.send("How active would you be if you became a member of staff here at Avenir?")
                    try:
                        srating = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        
                    await ctx.author.send("Do you unerstand that your application can be declined at any moment?")
                    try:
                        decline = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        
                    await ctx.author.send("Do you understand that you can be fired at any time and you will have to attend a training before you become a full staff member?")
                    try:
                        fire = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                            await ctx.author.send('Your application has been submit. [ Phase 1/3 ]')

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"New Staff Application")
        embed.add_field(name="Roblox username:", value=name.content, inline=False)
        embed.add_field(name="Reason for becoming staff:", value=reason.content, inline=False)
        embed.add_field(name="How they could benefit:" , value=benefit.content}", inline=False)
        embed.add_field(name="Activity before becoming staff:" , value =rating.content", inline=False)
        embed.add_field(name="Activity when staff:" , value =srating.content", inline=False)
        embed.add_field(name="Understanding of application declining:" , value =decline.content", inline=False)
        embed.add_field(name="Understand of firing and attending training:" , value =fire.content", inline=False)
        embed.set_footer(text=f"Sent by {ctx.author}")
        channel = self.bot.get_channel(794962966788702218)
        await channel.send(embed=embed)

    @ally.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You have recently applied for staff. Wait {(int(error.retry_after/20160))} minutes to retry.")


def setup(bot):
    bot.add_cog(marketplace(bot))
