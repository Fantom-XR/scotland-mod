import discord
from discord.ext import commands


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
    @commands.guild_only()
    async def announce(self,ctx, chan: discord.TextChannel, * , announcement=None):
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

def setup(bot):
    bot.add_cog(Cog(bot))