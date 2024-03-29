from modals.add_tasks import AddTaskModal, discord, db_, os


class LanguageButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Python",
        style=discord.ButtonStyle.gray,
        custom_id="1",
        emoji="<:py:1058018347947659324>",
    )
    async def python(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(AddTaskModal("python"))

    @discord.ui.button(
        label="C#",
        style=discord.ButtonStyle.gray,
        custom_id="2",
        emoji="<:cs:1058018616777383966>",
    )
    async def cs(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(AddTaskModal("cs"))

    @discord.ui.button(
        label="JAVA",
        style=discord.ButtonStyle.gray,
        custom_id="3",
        emoji="<:java:1058018677980667914>",
    )
    async def java(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(AddTaskModal("java"))

    @discord.ui.button(
        label="JS",
        style=discord.ButtonStyle.gray,
        custom_id="4",
        emoji="<:js:1058020780086140978>",
    )
    async def js(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(AddTaskModal("js"))

    @discord.ui.button(
        label="C++",
        style=discord.ButtonStyle.gray,
        custom_id="8",
        emoji="<:cpp:1192752241887682670>",
    )
    async def cpp(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(AddTaskModal("cpp"))

    @discord.ui.button(
        label="HTML CSS",
        style=discord.ButtonStyle.gray,
        custom_id="6",
        emoji="<:html_css:1061701991144894554>",
    )
    async def html_css(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await button.response.send_modal(AddTaskModal("html_css"))

    @discord.ui.button(
        label="MSSQL",
        style=discord.ButtonStyle.gray,
        custom_id="7",
        emoji="<:mssql:1070269021003468800>",
    )
    async def mssql(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_modal(AddTaskModal("mssql"))


