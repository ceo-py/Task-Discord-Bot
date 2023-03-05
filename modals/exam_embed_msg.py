import discord


class AddEmbedModal(discord.ui.Modal, title="Add additional information for Exam"):
    msg_text = discord.ui.TextInput(
        label="Custom message for embed when there are Exams",
        placeholder="Tyre message text here!",
        max_length=4000,
    )

    def __init__(self):
        super().__init__()

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Selected modules was disabled for searching!",
            ephemeral=True,
        )
