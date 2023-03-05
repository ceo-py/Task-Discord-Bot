from modals.ask_for_task_name import TaskName, discord


class LanguageSearchingButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Python",
        style=discord.ButtonStyle.gray,
        custom_id="100",
        emoji="<:py:1058018347947659324>",
    )
    async def python(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(TaskName("py"))

    @discord.ui.button(
        label="C#",
        style=discord.ButtonStyle.gray,
        custom_id="101",
        emoji="<:cs:1058018616777383966>",
    )
    async def cs(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(TaskName("cs"))

    @discord.ui.button(
        label="JAVA",
        style=discord.ButtonStyle.gray,
        custom_id="102",
        emoji="<:java:1058018677980667914>",
    )
    async def java(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(TaskName("java"))

    @discord.ui.button(
        label="JS",
        style=discord.ButtonStyle.gray,
        custom_id="103",
        emoji="<:js:1058020780086140978>",
    )
    async def js(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(TaskName("js"))

    @discord.ui.button(
        label="HTML CSS",
        style=discord.ButtonStyle.gray,
        custom_id="104",
        emoji="<:html_css:1061701991144894554>",
    )
    async def html_css(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await button.response.send_modal(TaskName("html"))

    @discord.ui.button(
        label="MSSQL",
        style=discord.ButtonStyle.gray,
        custom_id="105",
        emoji="<:mssql:1070269021003468800>",
    )
    async def mssql(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(TaskName("mssql"))
