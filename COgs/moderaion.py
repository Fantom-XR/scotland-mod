import discord
from discord.ext import commands
import asyncio


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    async def kick(self, ctx, member: discord.Member, * , reason = None):
        """|| Kicks a player (owner only)"""
        await member.send(f"you were kicked by {ctx.author.mention} for following resons(s) : {reason}")
        await member.kick(reason = reason)
        await ctx.send(f"{member.mention} was kick by {ctx.author.mention} reason : {reason}")
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    async def ban(self, ctx, member: discord.Member, * , reason = None):
        """"|| Bans a member"""
        await member.send(f"you were baned by {ctx.author.mention} for following reason(s) : {reason}")
        await member.ban(reason = reason)
        await ctx.send(f"{member.mention} was baned by {ctx.author.mention} reason : {reason}")
    
    @commands.command()
    @commands.has_guild_permissions(administrator = True)
    async def unban(self,ctx, *, member):
        """|| Unban command no need of mention use like Expressingames#2342"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

        
    @commands.command()
    @commands.has_guild_permissions(manage_messages= True)
    async def clear(self,ctx, amount=0):
        """
       || Deletes messages
        """
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    async def announce2(self,ctx, chan: discord.TextChannel, * , announcement=None):
        """|| announces something """
        if not announcement:
            await ctx.send("provide a announcement")
        await chan.send(f'{announcement}')

    @commands.command()
    @commands.has_guild_permissions(manage_messages= True)
    async def say(self,ctx, * , Text):
        await ctx.message.delete()
        await ctx.send(f"{Text}")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    async def dm(self,ctx, member: discord.Member, * , text=None):
        await member.send(f"{text}")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    async def announce(self,ctx, chan: discord.TextChannel, * , announcement=None):
        """|| announces something """
        if not announcement:
            await ctx.send("provide a announcement")
        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.add_field(name="Announcement" , value=announcement)
        embed.set_footer(text=f"Send by {ctx.author}")
        await chan.send(embed=embed)
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    async def banner(self, ctx,chan: discord.TextChannel, link, * , heading):
        await ctx.send("whats the discription?")
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
        try:
            item = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.send("Timed out")
        else:
            await ctx.send("DONE")

        embed= discord.Embed()
        embed.add_field(name=heading, value=item.content)
        embed.set_image(url=link)
        await chan.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def product(self, ctx, chan: discord.TextChannel):
        await ctx.send("Whats the product?")
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
        try:
            item = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.send("Timed out")
        else:
            await ctx.send("Whats the price?")
            try:
                price = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.send("Timed out")
            else:
                await ctx.send("Any note?")
                try:
                    note = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.send("Timed out")
                else:
                    await ctx.send("please provide a image (no links) ")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                        attachment = Image.attachments[0]
                        attachment_url = attachment.url
                    except asyncio.TimeoutError:
                        await ctx.send("Timed out")
                    else:
                        await ctx.send("DONE!")

        embed = discord.Embed()
        embed.set_author(name=f"Item")
        embed.add_field(name="product" , value=item.content)
        embed.add_field(name="Price" , value=price.content)
        embed.add_field(name="Note" , value=note.content)
        embed.set_image(url=attachment_url)
        await chan.send(embed=embed)

def setup(bot):
    bot.add_cog(Cog(bot))
