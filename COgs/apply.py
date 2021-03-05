import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def apply(self, ctx):
        await ctx.send('Check for a DM by <@814852722087034891>')
        await ctx.author.send("""**Scotland™ Staff Application**

Requirements:
- Your reputation must be clean.
- When applying, use full punctuation & grammar.
- Answer questions in detail and to the best of your ability
- Must be 13+ to apply
- Must be active

Say "next" to continue, or say "cancel" if you wish not to do the application.
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
                    await ctx.author.send("Do you know what to do as a staff member at Scotland™? If so please explain.")
                    try:
                        idk = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("Do you agree to all of our rules?")
                        try:
                            rating = await self.bot.wait_for('message', check=check, timeout=120)
                        except asyncio.TimeoutError:
                            await ctx.author.send("Timed out")
                        else:
                            await ctx.author.send('Your application has been submit. [ Phase 1/3 ] \n Phase 2 is more questions and an exam. \n Phase 3 is a trial phase')

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"New Application")
        embed.add_field(name="Experience:", value=price.content, inline=False)
        embed.add_field(name="Reasoning:", value=note.content, inline=False)
        embed.add_field(name="The role/responsibilities:", value=idk.content, inline=False)
        embed.add_field(name="Rules:", value=rating.content, inline=False)
        embed.set_footer(text=f"Sent by {ctx.author}")
        channel = self.bot.get_channel(817404938761535540)
        await channel.send(embed=embed)

  

def setup(bot):
    bot.add_cog(marketplace(bot))
