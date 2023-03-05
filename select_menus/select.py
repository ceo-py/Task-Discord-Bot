from modals.ask_for_task_name import discord
from modals.exam_embed_msg import AddEmbedModal


class Exam:
    def __init__(self):
        self.exam = []
        self.modules = []

    def add_exams(self, exams):
        self.exam += exams

    def clear_exams(self):
        self.exam = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self):
        self.modules = []


exams = Exam()

all_exams_to_skip = {
    "Basics": ["PB - Exams", "PB - More Exercises", "Basics"],
    "Fundamentals": ["Fundamentals"],
    "Advanced": ["Advanced"],
    "OOP": ["OOP"],
}


class SelectMenu(discord.ui.Select):
    info = [
        ("No Exam", "Enable all languages solutions for every module!", "\U0001F513"),
        ("Basics", "Disable all languages solutions for this module!", "\U0001F512"),
        (
            "Fundamentals",
            "Disable all languages solutions for this module!",
            "\U0001F512",
        ),
        ("Advanced", "Disable all languages solutions for this module!", "\U0001F512"),
        ("OOP", "Disable all languages solutions for this module!", "\U0001F512"),
    ]

    def __init__(self):
        options = [
            discord.SelectOption(label=label, description=description, emoji=emoji)
            for (label, description, emoji) in self.info
        ]

        super().__init__(
            placeholder="Pick a modules to disable / enable task solutions!",
            options=options,
            min_values=1,
            max_values=5,
        )

    async def callback(self, interaction: discord.Interaction):

        if "No Exam" in self.values and len(self.values) > 1:
            await interaction.response.send_message(
                content="You can't pick `No Exam` with any modules! Pick it alone to enable all solutions!!!",
                ephemeral=True,
            )

        elif self.values[0] == "No Exam":
            exams.clear_exams()
            exams.remove_module()

            await interaction.response.send_message(
                content="Every solution is free for search!", ephemeral=True
            )

        else:
            exams.clear_exams()
            exams.remove_module()

            for module in all_exams_to_skip:
                if module in self.values:
                    exams.add_exams(all_exams_to_skip[module])
                    exams.add_module(module)

            await interaction.response.send_message(
                content=f'Selected modules was disabled for searching! -> {", ".join(exams.modules)}',
                ephemeral=True,
            )


class Select(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectMenu())
