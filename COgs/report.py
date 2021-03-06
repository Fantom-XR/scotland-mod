import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def report(self, ctx):
        await ctx.send('Check for a DM by <@814857112458100736>')
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
                        reason = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                       await ctx.author.send("Please provide an image, not a link.")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                        attachment = Image.attachments[0]
                        attachment_url = attachment.url
                    except asyncio.TimeoutError:
                        await ctx.author.send("Timed out")
                    else:
                            await ctx.author.send('Your report has been submit.]')

embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"New Report")
        embed.add_field(name="Name:", value=price.content, inline=False)
        embed.add_field(name="Reported user:", value=note.content, inline=False)
        embed.add_field(name="Reason:", value=reason.content, inline=False)
        embed.set_image(url=attachment_url)
        embed.set_footer(text=f"Sent by {ctx.author}")
        channel = self.bot.get_channel(817727667196919809)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(report(bot))
