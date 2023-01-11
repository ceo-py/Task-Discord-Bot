from database.data_base import db_
from text_cleaning.string_cleaning import StringCleaning as Sc


async def look_for_answer(question, language):
    search_for = await Sc.clean_input(question)
    find_tasks = await db_.find_tasks(language, search_for)
    result = []

    for show in find_tasks:
        if sum(len(x) for x in result) <= 3850:
            result.append(
                f"[{await Sc.prepare_text_for_output(show['task name'])}]({show['task url']})"
            )
        else:
            break

    return "\n".join(result)
