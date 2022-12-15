from requests_html import HTMLSession
import json

url_start = "https://github.com/ceo-py/softuni/tree/main/Python%20Advanced/Python%20Advanced%20-%20Exams"
session = HTMLSession()


def getdata(url):
    r = session.get(url)
    return r


htmldata = getdata(url_start)
my_links = []
check_url = {}


def get_all_directories(url_start):
    htmldata = getdata(url_start)
    links = htmldata.html.absolute_links
    for info in links:
        if "/tree/main/" in info != check_url.get(info):
            check_url[info] = info
            get_all_directories(info)
        elif ".py" in info:
            my_links.append(info)


def write_json(data, filename="python_data.json"):
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

with open("python_data.json", "r+", encoding='utf-8') as json_file:
    data = json.load(json_file)
    data.update(links_for_bd)

write_json(data)

print(len(my_links))
