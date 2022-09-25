import traceback

import discord

from . import config


options1 = []

for label, value in config.options1:
    options1.append(discord.SelectOption(label=label, value=str(value)))


class ButtonView1(discord.ui.View):
    def __init__(self, bot):
        self.value = None
        self.bot = bot
        self.guild = self.bot.get_guild(config.guild_id)
        self.role = self.guild.get_role(config.role_id)
        self.log_channel = self.bot.get_channel(config.log_channel_id)
        super().__init__(timeout=None)

    @discord.ui.button(label='Verify', style=discord.ButtonStyle.blurple, custom_id='button-1')
    async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        try:
            await interaction.user.add_roles(self.role)
            await interaction.response.send_message(f'You are verified! Go to <#{config.select_channel_id}> and select your role.\n認証されました！<#{config.select_channel_id}>に移動してロールを選択してください。', ephemeral=True)
        except Exception as e:
            traceback.print_exception(e)
            await self.log_channel.send(f'{interaction.user.mention} への会員ロールの付与に失敗しました\n```\n{str(e)}\n```')


class SelectView1(discord.ui.View):
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.guild = self.bot.get_guild(config.guild_id)
        self.roles = {}
        for _, value in config.options1:
            self.roles[value] = self.guild.get_role(value)
        return super().__init__(timeout=None)

    @discord.ui.select(placeholder='役割を選択してください', custom_id='select-1', min_values=0, max_values=len(options1), options=options1)
    async def select_callback(self, select: discord.ui.Select, interaction: discord.Interaction):
        added_roles = []
        removed_roles = []
        for _, value in config.options1:
            if str(value) in select.values:
                added_roles.append(self.roles[int(value)])
            else:
                removed_roles.append(self.roles[int(value)])
        await interaction.user.add_roles(*added_roles)
        await interaction.user.remove_roles(*removed_roles)
        await interaction.response.send_message('役割を選択しました。', ephemeral=True)
