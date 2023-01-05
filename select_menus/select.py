class SelectMenu(discord.ui.Select):
    info = [
        ("Python", "More information", '\U0001F4D9'), ("C#", "More information", '\U0001F4D9')
    ]

    def __init__(self):
        options = [discord.SelectOption(label=label, description=descri, emoji=emoji) for (label, descri, emoji) in
                   self.info]

        super().__init__(placeholder="Choose Wisely:", options=options, min_values=1, max_values=2)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=" ".join(self.values), view=Selected(), ephemeral=True)


class SelectedTest(discord.ui.Select):
    additional_info = {
        "Python": {
            "Book 1": "Book 1",
            "Book 2": "Book 2"

        }
    }

    def __init__(self, options):
        super().__init__(placeholder="Books", options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=" ".join(self.values), view=Selected(), ephemeral=True)


class Selected(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectedTest([discord.SelectOption(label=name) for name in ["book1", "book2"]]))


class Select(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectMenu())


@client.tree.command(name="test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(content="test", view=Select())