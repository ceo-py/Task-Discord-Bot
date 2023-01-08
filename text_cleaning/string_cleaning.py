from string import capwords


class StringCleaning:
    @staticmethod
    async def clean_input(data):
        search_for = " ".join(data)
        search_for = (
            search_for.rstrip()
            .lstrip()
            .replace(". ", "_")
            .replace(" ", "_")
            .replace("-", "_")
            .replace("'", "")
            .lower()
        )
        if search_for.startswith("0"):
            search_for = search_for.replace("0", "")
        return search_for

    @staticmethod
    async def prepare_text_for_output(text):
        return capwords(text.replace("_", " "))
