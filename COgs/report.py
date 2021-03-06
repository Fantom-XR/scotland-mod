import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def report(self, ctx):
        await ctx.send('Check for a DM by <@681537574593888336>')
        await ctx.author.send("""**REPORTING SYSTEM**
        
Information:
- Your report must be fact based
- You must provide proof in your report
- False reports will result in a consequence

Say "next" to continue, or say "cancel" if you wish not to make a report.
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
                await ctx.author.send("Please state the Discord Username id eg. <@[ID here]> of the person you are reporting.")
                try:
                    note = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                else:
                    await ctx.author.send("What are you reporting this user for?")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("Please submit proof of these accusations.")
                        try:
                            rating = await self.bot.wait_for('message', check=check, timeout=120)
                        except asyncio.TimeoutError:
                            await ctx.author.send("Timed out")
                        else:
                            await ctx.author.send('Your report has been submit.]')

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"New Report")
        embed.add_field(name="Name:", value=price.content, inline=False)
        embed.add_field(name="Reported user:", value=note.content, inline=False)
        embed.add_field(name="Report Reasoning:" , value =f"{Image.content}", inline=False)
        embed.add_field(name="Proof:" , value =f"{rating.content}", inline=False)
        embed.set_footer(text=f"Sent by {ctx.author}")
        channel = self.bot.get_channel(817727667196919809)
        await channel.send(embed=embed)

    @ally.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You have recently submit a report. Wait {(int(error.retry_after/60))} minutes to retry.")


def setup(bot):
    bot.add_cog(marketplace(bot))
