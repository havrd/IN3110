import requesting_urls as ru
import filter_urls as fu
from collections import deque
import os


BASE_URL = "https://en.wikipedia.org"

def find_path(start, end):
    """
    Find the shortest path from one wiki url to another with BFS
    Args:
        start (str): the wikipedia url to start from
        end (str): the goal
    Returns:
        list (list): a list containing the path from start to end
    """
    path = {}
    path[start] = [start]

    queue = deque()
    queue.append(start)

    while queue:
        s = queue.popleft()
        print(s)
        article = ru.get_html(s)
        urls = fu.find_articles(article, base_url=BASE_URL)
        valid_urls = [x for x in urls if x.startswith("https://en.wikipedia.org/wiki/")]

        for url in valid_urls:
            if url == end:
                os.makedirs("wiki_race_challenge", exist_ok=True )
                with open(f"./wiki_race_challenge/shortest_way.txt", "w") as out_file:
                    for link in path[s]:
                        out_file.write(f"{link}\n")
                    out_file.write(f"{url}")
                return path[s] + [url]
            if url not in path and s != url:
                path[url] = path[s] + [url]
                queue.append(url)

start = "https://en.wikipedia.org/wiki/Nobel_Prize"
end = "https://en.wikipedia.org/wiki/Array_data_structure"

#start ="https://en.wikipedia.org/wiki/%C3%98vre_Sandsv%C3%A6r"
#end = "https://en.wikipedia.org/wiki/List_of_municipalities_of_Norway"


print(find_path(start, end))
