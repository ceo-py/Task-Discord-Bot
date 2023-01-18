from discord.ext import commands

from buttons.searching_task_buttons import LanguageSearchingButtons
from buttons.language_buttons import LanguageButtons, discord, os
from prepare_answer.generate_message import show_result_message
from stats.add_stats_json import load_stats


class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()

        super().__init__(command_prefix="?", help_command=None, intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(LanguageButtons())
        self.add_view(LanguageSearchingButtons())


client = PersistentViewBot()


@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.Game(name="On your demand!!!"))
    print("Ready")


@client.command()
async def add(ctx):
    if str(ctx.author) in os.getenv("OWNER"):
        await ctx.send(
            embed=discord.Embed(
                colour=discord.Colour.blue(),
                title="** Click on language to add task in database ** :warning: ",
            ),
            view=LanguageButtons(),
        )


@client.command(aliases=["py", "cs", "java", "js", "html"])
async def task(ctx, *task):

    if ctx.invoked_with == "task":
        await ctx.author.send(embed=embed_for_itask(), view=LanguageSearchingButtons())
        return

    await ctx.author.send(embed=await show_result_message(task, ctx.invoked_with))


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Have no fear - I task is here!",
        description="My master has taught few commands to aid you with your SoftUni coding adventure:",
        colour=discord.Colour.gold(),
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/983670671647313930/994162444467445870"
        "/pnghut_customer-service-technical-support.png"
    )
    embed.add_field(
        name=f"?py task name - for Python\n?cs task name - for C#\n"
        f"?java task name - for Java\n"
        f"?js task name - for JavaScript\n"
        f"?html task name - for html and css",
        value=f"```fix\nWhen you ask me for a task by its full name "
        f"(or at least part of its name) I will search for it and show you the results. "
        f"If you are not sure how to ask me - see the example below.```[Command example]("
        f"https://cdn.discordapp.com/attachments/983670671647313930/1056160608917131294/image.png)",
        inline=False,
    )
    embed.add_field(
        name="/itask",
        value="```fix\nThis command will bring menu with all languages that currently are supported for "
        "task"
        "searching.```",
    )
    embed.add_field(
        name=f"?help",
        value=f"```fix\nHave no fear - I task is here! Oops - I have said that already, ain't I? "
        f"Well...  if you see this, then you are looking at my ?help, so enjoy it!```",
        inline=False,
    )
    await ctx.author.send(embed=embed)


@client.tree.command(
    name="percent", description="Link with info about calculating percents!"
)
async def percent(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Как да изчисляваме проценти!",
        description="**Подробна информация** [ТУК](https://www.kaksepravibg.com/kak-se-izchisliava-procent/?fbclid"
        "=IwAR1vuZo1zZnaW0eAZnlhTT3ClPxMtojowO1Y9ORzrqc1OfH4-3XSTe-PjcY)",
        colour=discord.Colour.gold(),
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/983670671647313930/1061681874239500358/pngegg_1.png"
    )
    embed.add_field(
        name="**Пример: 1**",
        value="Имаме 10 ябълки. 10 ябълки са 100%. Изяждаме 2 ябълки. От тук следва, че сме изяли **__2 / 10 х 100% = "
        "20%__**"
        "от ябълките и оставаме с 80% от първоначалния брой ябълки."
        " От този пример можем да изведем формулата за смятане на процент от число"
        " процент от цяло = **__част х 100 / цялото__**"
        " или в нашия пример:"
        " **__20%  = 2 ябълки х 100  / 10 ябълки__**",
        inline=False,
    )
    embed.add_field(
        name="**Пример: 2**",
        value="Имаме промоция 8% на стока на цена 200 лв. Използваме следната формула:"
        " **__200 х 8 / 100 = 16 лв__**. Следователно цената на стоката е 184 лв.",
        inline=False,
    )
    embed.add_field(
        name="**Намиране на число по даден процент**",
        value="Ако сме закупили стока, намалена с 20% и сме платили цена от 160 лв, колко е била цената на стоката "
        "без намалението. Намалението е било 20%, следователно сме платили 80% от цената на стоката. Стоката е "
        "струвала Х лева. Смятаме по формулата: **__80 / 100 * Х = 160__** Като пресметнем уравнението, "
        "се получава, че цената преди намалението е била 200 лв.",
        inline=False,
    )
    await interaction.response.send_message(embed=embed)


@client.tree.command(
    name="itask", description="It will show you how to use the bot for task solutions."
)
async def itask(interaction: discord.Interaction):
    embed = embed_for_itask()

    await interaction.response.send_message(
        embed=embed, view=LanguageSearchingButtons()
    )


@client.command()
async def stats(ctx):
    if str(ctx.author) in os.getenv("OWNER"):
        data = await load_stats()
        embed = discord.Embed(
            title=f":warning:Total Answers:warning:",
            description=f"{sum(data.values())}",
            colour=discord.Colour.blue(),
        )
        await ctx.author.send(embed=embed)


def embed_for_itask():
    embed = discord.Embed(
        title="Показвам примерни решения на задачите от СофтУни!",
        description="Изберете езика за който желаете да намерите пример и напишете името на задача.\n"
        "Ако желаете може да ми задавате въпроси на лично съобщение с команда за съответния език "
        "`?py`, `?cs`, `?java` или `?html` и името на задачата.",
        colour=discord.Colour.gold(),
    )
    return embed


client.run(os.getenv("TOKEN"))
