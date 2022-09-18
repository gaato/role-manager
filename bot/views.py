import discord

from . import config


options = []

for label, value in config.options:
    options.append(discord.SelectOption(label=label, value=str(value)))


class RoleSelectView(discord.ui.View):
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.guild = self.bot.get_guild(config.guild_id)
        self.roles = {}
        for _, value in config.options:
            self.roles[value] = self.guild.get_role(value)
        return super().__init__(timeout=None)

    @discord.ui.select(placeholder='役割を選択してください', custom_id='role_select', min_values=0, max_values=len(options), options=options)
    async def select_callback(self, select, interaction: discord.Interaction):
        added_roles = []
        removed_roles = []
        for _, value in options:
            if str(value) in select.values:
                added_roles.append(self.roles[int(value)])
            else:
                removed_roles.append(self.roles[int(value)])
        await interaction.user.add_roles(*added_roles)
        await interaction.user.remove_roles(*removed_roles)
        await interaction.response.send_message('役割を選択しました。', ephemeral=True)
