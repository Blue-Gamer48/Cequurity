from datetime import datetime
import discord
from discord.ext import commands
from discord import (Modal,TextInput)
class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_user = None
    @commands.Cog.slash_command(name="test", description="Kleiner Funktionstest")
    async def test(self, ctx):
        await ctx.respond("Test Bestanden")
    @commands.Cog.slash_command(name="create_embed",description="erstelle ein Custom Embed")
    async def create_embed(self, ctx):
        create_embed_modal = Modal(custom_id='create_embed',title='Embed Maker.',components=[TextInput(custom_id='Title',label="Titel",style=1,min_length=0,placeholder='Wähle den Title des Embeds'),
                                                                                       TextInput(custom_id='Text',label="Text", style=1,min_length=0,placeholder='Schreib was als Text im Embed Stehen Soll'),
                                                                                       TextInput(custom_id='Foother',label="Foother",style=2,min_length=0,placeholder='Schreib was im Foother Stehen Soll',required=False)])
        await ctx.respond_with_modal(modal=create_embed_modal)
    @commands.Cog.on_submit(custom_id='create_embed')
    async def create_embed_modal_callback(self, i: discord.ModalSubmitInteraction):
        Title = i.get_field(custom_id="Title").value
        Text = i.get_field(custom_id="Text").value
        Foother = i.get_field(custom_id="Foother").value
        try:
            embed_ec_succes = discord.Embed(title=f"{Title}",description=f"{Text}", color=0x3498bd)
            embed_ec_succes.set_footer(text=f"{Foother}",icon_url="https://cdn.discordapp.com/avatars/792484163684532274/a1b1511a7333bf989f1a170012b11806.webp?size=1024")
            await i.respond(embed=embed_ec_succes)
        except Exception as exc:
            embed_error_ec = discord.Embed(title="Fehler",description=f"Es sieht so aus, als wäre etwas schief gelaufen:\n{exc}", color=discord.Colour.red())
            await i.respond(embed=embed_error_ec)
            raise exc
        else:
            embed_ec_succes_usr = discord.Embed(title="Embed Erstellt",description="Embed wurde Erfolgreich erstellt",colour=discord.Color.green())
        await i.respond(embed=embed_ec_succes_usr,hidden=True)

def setup(bot):
    bot.add_cog(cmds(bot))