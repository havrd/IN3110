import re
import requesting_urls as ru
import pathlib
import os


def find_urls(html_str, base_url=None, output=None):
    """
    Finds all urls in a given html page
    Args:
        html_str (str): The html page to extract urls from
        base_url (str): base url so that all urls will be found
        output (str): filename return_list will be saved as
    Returns:
        return_list (list): list of urls found
    """

    return_list = []
    if base_url != None:
        urls = re.findall(r'<a[^>]+href="(\/[^\/][^":#>]+)(?:#|")', html_str, flags=re.IGNORECASE)
        for url in urls:
            url = base_url+url
            return_list.append(url)
        urls = re.findall(r'<a[^>]+href="(\/\/[^":#>]+\.[^":#>]+)(?:#|")', html_str, flags=re.IGNORECASE)
        for url in urls:
            url = "https:"+url
            return_list.append(url)
    urls = re.findall(r'<a[^>]+href="(https:\/\/[^":#>]+\.[^":#>]+)(?:#|")', html_str, flags=re.IGNORECASE)
    return_list = return_list + urls
    return_list = list(set(return_list))

    if output!=None:
        write_to_file(return_list, output)

    return return_list


def find_articles(html_str, output=None, base_url=None):
    """
    Finds all wikipedia urls in a given html page
    Args:
        html_str (str): The html page to extract urls from
        base_url (str): base url so that all urls will be found
        output (str): filename wiki_urls will be saved as
    Returns:
        wiki_urls (list): list of wikipedia urls found
    """

    urls = find_urls(html_str, base_url=base_url)
    wiki_urls = []
    regex = r'https:\/\/[\w-]{2,}\.wikipedia\.org.+'
    for url in urls:
        match = re.search(regex, url, flags=re.IGNORECASE)
        if match!=None:
            wiki_urls.append(url)

    if output!=None:
        write_to_file(wiki_urls, output)
    return wiki_urls



def write_to_file(list, output):
    """
    Support function to write a list of urls to a file
    Args:
        list (str): list of urls
        output (str): filename list will be saved as
    """

    this_path = pathlib.Path(__file__).parent.resolve()
    rel_path = "filter_urls/"+output
    path = os.path.join(this_path, rel_path)
    if os.path.exists(path):
        os.remove(path)
    f = open(path, "w")
    for url in list:
        f.write(url+'\n')
    f.close()


def test_find_urls():
    """
    Test all functions on three different urls
    Args:
        None
    Returns:
        None
    """

    nobel = ru.get_html("https://en.wikipedia.org/wiki/Nobel_Prize")
    bundes = ru.get_html("https://en.wikipedia.org/wiki/Bundesliga")
    ski = ru.get_html("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup")

    find_urls(nobel, output="nobel_urls.txt", base_url="https://en.wikipedia.org/")
    find_urls(bundes, output="bundes_urls.txt", base_url="https://en.wikipedia.org/")
    find_urls(ski, output="ski_urls.txt", base_url="https://en.wikipedia.org/")
    find_articles(nobel, output="nobel_articles.txt", base_url="https://en.wikipedia.org/")
    find_articles(bundes, output="bundes_articles.txt", base_url="https://en.wikipedia.org/")
    find_articles(ski, output="ski_articles.txt", base_url="https://en.wikipedia.org/")


test_find_urls()
