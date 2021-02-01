import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def apply(self, ctx):
        await ctx.send('Check for a DM by <@788510771503693854>')
        await ctx.author.send("""**Avenir Staff Application**
        
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
            await ctx.author.send("Have you got any past experience?")
            try:
                price = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("How can you benefit us?")
                try:
                    note = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                else:
                    await ctx.author.send("Do you know what to do as customer service? If so please explain.")
                    try:
                        idk = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("Do you agree to all of our rules and terms of services?")
                        try:
                            rating = await self.bot.wait_for('message', check=check, timeout=120)
                        except asyncio.TimeoutError:
                            await ctx.author.send("Timed out")
                        else:
                            await ctx.author.send('Your application has been submit. [ Phase 1/3 ]')

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"New Application")
        embed.add_field(name="Experience:", value=price.content, inline=False)
        embed.add_field(name="Reasoning:", value=note.content, inline=False)
        embed.add_field(name="The role/responsibilities:", value=idk.content, inline=False)
        embed.add_field(name="Rules & TOS:", value=rating.content, inline=False)
        embed.set_footer(text=f"Sent by {ctx.author}")
        channel = self.bot.get_channel(794962966788702218)
        await channel.send(embed=embed)

  

def setup(bot):
    bot.add_cog(marketplace(bot))
