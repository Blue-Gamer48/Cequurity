from datetime import datetime
import discord
from discord.ext import commands
from discord import (Modal,TextInput)
from discord import Button
components = [
    [discord.Button(
        label="verify_btn",
        emoji="✅",
        style=discord.ButtonColor.green,
        custom_id="verify-btn")]]
class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_user = None
    @commands.Cog.slash_command(name="verify",description="Sendet das Verify Panel")
    async def verify(self,ctx):
        embed=discord.Embed(title="Richtlinien",color=0x3498bd)
        embed.add_field(name="1.",value="Höfflichkeit wird von jedem Servermitglied stets erwartet. Außerdem sollte man eine anständige Wortwahl haben und keine Respektlosigkeit zeigen.")
        embed.add_field(name="2.",value="Jegliche art von Verletzungen wie Beleidigung, Belästigung, Mobbing, oder auch Rassismus wird strengstens untersagt. Brutale, pornographische oder andere unangebrachte Inhalte gehören ebenfalls dazu.")
        await ctx.send(embed=embed,components=components)
    @commands.Cog.on_click(custom_id='verify_btn')
    async def userinfo_button(self, ctx, _):
        await ctx.send("verify Erfolgreich")
def setup(bot):
    bot.add_cog(cmds(bot))