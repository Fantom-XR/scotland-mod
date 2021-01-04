import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def hire(self, ctx):
        await ctx.send('Look for a DM by <@788510771503693854>')
        await ctx.author.send("Who are you trying to hire? [ Builder, Scripter etc. ]")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            hire = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.author.send("Describe the work that needs to be done.")
            try:
                notes = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("How much are you willing to pay?")
                try:
                    price = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("time out!")
                else:
                    await ctx.author.send("Your advert has been published! Look in <#789541244380381205>")
                

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name="🧳 Hiring")
        embed.add_field(name="Name:", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="Looking for a:", value=hire.content, inline=False)
        embed.add_field(name="Payment:", value=price.content, inline=False)
        embed.add_field(name="Work needed:", value=notes.content, inline=False)
        channel = self.bot.get_channel(789541244380381205)
        await channel.send(embed=embed)



    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def ad(self, ctx):
        await ctx.send('Look for a DM by <@788510771503693854>')
        await ctx.author.send("What is the name of your business?")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            name = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.author.send("Give a description on what your group does.")
            try:
                notes = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("Provide link(s) related to your group.")
                try:
                    price = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("time out!")
                else:
                    await ctx.author.send("Provide an image, not a link.")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                        attachment = Image.attachments[0]
                        attachment_url = attachment.url
                    except asyncio.TimeoutError:
                        await ctx.author.send("Timed out")
                    else:
                        await ctx.author.send("Your advert has been published! Look in <#789541041631395890>")
                
        
        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"🖥️ Advertisement")
        embed.add_field(name="Group Name", value=name.content, inline=False)
        embed.add_field(name="Description", value=notes.content, inline=False)
        embed.add_field(name="Link(s)" , value =f"{price.content}", inline=False)
        embed.set_image(url=attachment_url)
        embed.set_footer(text=f"Sent by {ctx.author}")
        channel = self.bot.get_channel(789541041631395890)
        await channel.send(embed=embed)
        
        

    @sell.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"❌ This command is time-locked. Please wait {(int(error.retry_after/60))} minutes before retrying.")

    @hire.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"❌ This command is time-locked. Please wait {(int(error.retry_after/60))} minutes before retrying.")

    @ad.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"❌ This command is time-locked. Please wait {(int(error.retry_after/60))} minutes before retrying.")

def setup(bot):
    bot.add_cog(marketplace(bot))
