import discord
from database.data_base import db_, os


class AddTaskModal(discord.ui.Modal, title="Add task to database"):
    task_name = discord.ui.TextInput(
        label="Task name from Judge",
        placeholder="Replace space and extra characters with _",
        max_length=40,
    )
    task_urls = discord.ui.TextInput(
        label="Task URL",
        placeholder="Paste the URL link on the task solution",
        max_length=500,
    )

    def __init__(self, language):
        super().__init__()
        self.language = language

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"{await db_.add_task_to_db(self.language, self.task_name.value, self.task_urls.value)}",
            ephemeral=True,
        )
