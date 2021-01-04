import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def sell(self, ctx):
        await ctx.send('Look for a DM by <@681537574593888336>')
        await ctx.author.send("What product is being sold?")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            item = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.author.send("How much are you selling this for?")
            try:
                price = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("What features does this product have?")
                try:
                    note = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                else:
                    await ctx.author.send("Please provide an image, not a link.")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                        attachment = Image.attachments[0]
                        attachment_url = attachment.url
                    except asyncio.TimeoutError:
                        await ctx.author.send("Timed out")
                    else:
                        await ctx.author.send("Your advert has been published! Look in <#724241250764455957>")

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name="🛎️ Product Advertisement")
        embed.add_field(name="Product:", value=f"{item.content}", inline=False)
        embed.add_field(name="Sold by:", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="Price:", value=f"{price.content}", inline=False)
        embed.add_field(name="Features:", value=f"{note.content}", inline=False)
        embed.set_image(url=attachment_url)
        channel = self.bot.get_channel(724241250764455957)
        await channel.send(embed=embed)

    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def hire(self, ctx):
        await ctx.send('Look for a DM by <@681537574593888336>')
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
                    await ctx.author.send("Your advert has been published! Look in <#724241277826105374>")
                

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name="🧳 Hiring")
        embed.add_field(name="Name:", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="Looking for a:", value=hire.content, inline=False)
        embed.add_field(name="Payment:", value=price.content, inline=False)
        embed.add_field(name="Work needed:", value=notes.content, inline=False)
        channel = self.bot.get_channel(724241277826105374)
        await channel.send(embed=embed)



    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def ad(self, ctx):
        await ctx.send('Look for a DM by <@681537574593888336>')
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
                        await ctx.author.send("Your advert has been published! Look in <#724241221395939330>")
                
        
        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"🖥️ Advertisement")
        embed.add_field(name="Group Name", value=name.content, inline=False)
        embed.add_field(name="Description", value=notes.content, inline=False)
        embed.add_field(name="Link(s)" , value =f"{price.content}", inline=False)
        embed.set_image(url=attachment_url)
        embed.set_footer(text=f"Sent by {ctx.author}")
        channel = self.bot.get_channel(724241221395939330)
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
