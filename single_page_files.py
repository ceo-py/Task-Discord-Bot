import json


with open("data.json", "r+", encoding='utf-8') as json_file:
    data = json.load(json_file)
    data_info = data["task"][0]

search_for = input()

search_for = search_for.rstrip().lstrip().replace(". ", "_").replace(" ", "_").replace("-", "_").lower()
if search_for.startswith("0"):
    search_for = search_for.replace("0", "")


try:
    print(data_info[search_for])
except KeyError:

    for task, url in data_info.items():
        if search_for[3:7] in task:
            print(task, url)




