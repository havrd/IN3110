import requests as req
import os
import pathlib


def get_html(url, params=None, output=None):
    """
    Extract date, venue and discipline for competitions.
    Args:
        url (str): The url to extract
        params (dictionary): passed on to the get function from requests
        output (str): filename string will be saved as
    Returns:
        html_str (str): Html page as a string
    """

    # passing the optional paramters argument to the get function
    response = req.get(url, params=params)
    html_str = response.text

    if output != None:
        this_path = pathlib.Path(__file__).parent.resolve()
        rel_path = "requesting_urls/"+output
        path = os.path.join(this_path, rel_path)
        if os.path.exists(path):
            os.remove(path)
        f = open(path, "w")
        f.write(html_str)
        f.close()
    return html_str

html_str = get_html("https://en.wikipedia.org/wiki/Studio_Ghibli", output="Studio_Ghibli.txt")
html_str = get_html("https://en.wikipedia.org/wiki/Star_Wars", output="Star_Wars.txt")
html_str = get_html("https://en.wikipedia.org/w/index.php", params={"title":"Main_page", "action":"info"}, output="index.txt")
