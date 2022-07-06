from requests_html import HTMLSession
import json

url_start = "https://github.com/ceo-py/softuni/tree/main/Fundamentals-Exams"
session = HTMLSession()


def getdata(url):
    r = session.get(url)
    return r


htmldata = getdata(url_start)
my_links = []
set_for_links = set()


def get_all_directories(url_start):
    htmldata = getdata(url_start)
    links = htmldata.html.absolute_links
    if ".py" in url_start:
        my_links.append(url_start)
        return

    for link in links:
        if link not in set_for_links:
            set_for_links.add(link)
            if "test.py" not in link and ("https://github.com/ceo-py/softuni/tree/main/" in link or
                                          "https://github.com/ceo-py/softuni/blob/main/" in link):
                get_all_directories(link)


def write_json(data, filename="data.json"):
    with open(filename, "w", encoding='utf-8') as x:
        json.dump(data, x, indent=9)


links_for_bd = {}
get_all_directories(url_start)
for task in my_links:
    print(task)
    taks_start_index = task.rfind("/") + 1
    task_name = task[taks_start_index:-3]
    links_for_bd[task_name] = task
    print(task_name)

with open("data.json", "r+", encoding='utf-8') as json_file:
    data = json.load(json_file)
    data_info = data["task"][0]
    data_info.update(links_for_bd)

write_json(data)

print(len(my_links))
