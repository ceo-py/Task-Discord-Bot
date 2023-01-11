import discord

from prepare_answer.generate_message import show_result_message
from prepare_answer.looking_for_answer import look_for_answer


class TaskName(discord.ui.Modal, title="Търсене на примерни решения!"):
    task_name = discord.ui.TextInput(
        label="Името на задачата в SoftUni Judge?",
        placeholder="Напишете част или цялото име на задачата",
        max_length=15,
    )

    def __init__(self, language):
        super().__init__()
        self.language = language

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            embed=await show_result_message((self.task_name.value,), self.language),
            ephemeral=True,
        )
