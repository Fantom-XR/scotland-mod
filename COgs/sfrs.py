import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def sfrs(self, ctx):
        await ctx.send('Check for a DM by <@814857112458100736>')
        await ctx.author.send("""**SFRS Application**

Hello, This is the Application for SFRS, Take your Time, Be Honest.


Do not ask for anyone to read your Application.

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
            await ctx.author.send("ROBLOX Username")
            try:
                name = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("How active are you on a scale of 1-10? \n 1 = Not very active \n 10 = Acitve")
                try:
                    activity = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                else:
                    await ctx.author.send("Why do you want to be apart of SFRS?")
                    try:
                        part = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("DO you have any Experience of being a Fire Fighter? \n Yes, No, Maybe")
                        try:
                            expereince = await self.bot.wait_for('message', check=check, timeout=120)
                        except asyncio.TimeoutError:
                            await ctx.author.send("Timed out")
                        else:
                            await ctx.author.send("If yes Please Explain \n *If you picked no please say N/A.*")
                    try:
                        expereince1 = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("What equipment is in a Fire Engine?")
                    try:
                        equipment = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                             await ctx.author.send("Tell Me More about yourself")
                    try:
                        them = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                                await ctx.author.send("Why would you be a good FIrefighter?")
                    try:
                        good = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                               await ctx.author.send("Do you have the Traits of a Firefighter? \n Yes, No, Maybe")
                    try:
                        traits = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                                   await ctx.author.send("Do you promise not to abuse Lights and Siren? \n Yes, No, Maybe")
                    try:
                        lights = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        
                                   await ctx.author.send("What can you bring to the Team of SFRS?")
                    try:
                        bring = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                                                           await ctx.author.send("What would you do if there was a Structure Fire (Explain in 100+ Words)")
                    try:
                        structure = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("What would you do if you see a Firefighter uses abusive language?")
                    try:
                        lang = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                                  await ctx.author.send("Do you understand that if you get pulled over by a member of PSOS you have to Pullover? \n Yes, No, Maybe")
                    try:
                        psos = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                                await ctx.author.send("Would you agree to be active on SFRS at least 3 times a week? \n Yes, No")
                    try:
                        active = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                                                        await ctx.author.send("Do you understand that you have to call Bronze Command+ Sir or Ma'am? \n Yes, No")
                    try:
                        bronze = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("Is there anything you would like to say? If no please put no.")
                    try:
                        extra = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                            await ctx.author.send('Your application response has been recorded, you will recive a DM once a member of the SFRS command have read it.')

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"New Application")
        embed.add_field(name="ROBLOX Username", value=name.content, inline=False)
        embed.add_field(name="How active are you on a scale of 1-10?", value=activity.content, inline=False)
        embed.add_field(name="Why do you want to be apart of SFRS?", value=part.content, inline=False)
        embed.add_field(name="Do you have any Experience of being a Fire Fighter?", value=expereince.content, inline=False)
        embed.add_field(name="If yes Please Explain", value=expereince1.content, inline=False)
        embed.add_field(name="What equipment is in a Fire Engine?", value=equipment.content, inline=False)
        embed.add_field(name="Tell Me More about yourself", value=them.content, inline=False)
        embed.add_field(name="Why would you be a good FIrefighter?", value=good.content, inline=False)
        embed.add_field(name="DO you have the Traits of a Firefighter?", value=traits.content, inline=False)
        embed.add_field(name="Do you promise not to abuse Lights and Siren?", value=lights.content, inline=False)
        embed.add_field(name="What can you bring to the Team of SFRS?", value=bring.content, inline=False)
        embed.add_field(name="What would you do if there was a Structure Fire (Explain in 100+ Words)", value=structure.content, inline=False)
        embed.add_field(name="What would you do if you see a Firefighter uses abusive language?", value=lang.content, inline=False)
        embed.add_field(name="DO you understand that if you get pulled over by a member of PSOS you have to Pullover?", value=psos.content, inline=False)
        embed.add_field(name="Would you agree to be active on SFRS at least 3 times a week?", value=active.content, inline=False)
        embed.add_field(name="Do you understand that you have to call Bronze Command+ Sir or Ma'am?", value=bronze.content, inline=False)
        embed.add_field(name="Is there anything you would like to say?", value=extra.content, inline=False)
        embed.set_footer(text=f"Sent by {ctx.author}")
        channel = self.bot.get_channel(818090072955420734)
        await channel.send(embed=embed)

  

def setup(bot):
    bot.add_cog(marketplace(bot))
