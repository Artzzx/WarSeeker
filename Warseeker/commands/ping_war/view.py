import discord
from discord.ext import commands
from discord import app_commands
from discord.embeds import Embed
import os

class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
                discord.SelectOption(label='Brightman', emoji='<:coc_brightman:1146068859875491880>'),
                discord.SelectOption(label='Brightman Jr', emoji='<:coc_brightmanjr:1146068946181685248>'),
                discord.SelectOption(label='Brightman / / /', emoji='<:coc_brightman3:1146068455376818297>'),
                discord.SelectOption(label='BigGuns', emoji='<:coc_bigguns:1144404447670304843>'),
            ]
        super().__init__(placeholder='Select an option...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        clan_name = self.values[0]
        await interaction.response.send_message(f"You have selected: {clan_name}")

class SelectMenuView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())

class ApplyView(discord.ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timeout = None

    @discord.ui.button(label="Check War", style=discord.ButtonStyle.green, custom_id="war")
    async def callback(self, interaction, button):
        select_menu_view = SelectMenuView()
        await interaction.response.send_message("Choose a clan from the dropdown:", view=select_menu_view, ephemeral=True)

class war_ping_view(commands.Cog):
    @app_commands.command(name="war_ping")
    async def cmd_apply(self, interaction: discord.Interaction):
        member = interaction.user
        
        leader_role = int(os.getenv("LEADER_ROLE_ID"))
        leader_role = member.guild.get_role(leader_role)
        
        if leader_role in member.roles:
            embed = Embed(title="War seeker attack checker", description="If you wish to check attack state of your clan current war please click here", color=0x0068cf)
            apply_view = ApplyView()
            await interaction.response.send_message(view=apply_view, embed=embed)
        else:
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)



    

    
