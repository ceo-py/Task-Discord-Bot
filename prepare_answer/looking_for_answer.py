from database.data_base import db_
from text_cleaning.string_cleaning import StringCleaning as Sc
from string import capwords

async def look_for_answer(question: str, language: str, skip_moduls: object) -> str:
    search_for = await Sc.clean_input(question)
    find_tasks = await db_.find_tasks(language, search_for)
    result = []

    for show in find_tasks:
        number, title = show['task name'].split('_')[0],  capwords((' ').join(show['task name'].split('_')[1:]))
        if sum(len(x) for x in result) <= 3650 and not exams(
            show["task url"], skip_moduls.exam
        ):
            result.append(
                f"{number}. [{title}]({show['task url']})"
            )
        else:
            break

    if skip_moduls.modules:
        result.append(
            f'\n\nВ момента се провеждат изпити по следните модули: `{", ".join(skip_moduls.modules)}`. С цел да '
            f"се осигури нормалното протичане на изпита, показване на решения от въпросните модули е изключено, до приключването им."
        )

    return "\n".join(result)


def exams(url: str, skip_moduls) -> bool:
    return any(x in url for x in skip_moduls)
