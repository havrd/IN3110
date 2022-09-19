from bs4 import BeautifulSoup
from requesting_urls import get_html
import filter_urls as fu
import re
import collections
import matplotlib.pyplot as plt


def extract_teams():
    """
    Extract team names and urls from the NBA Playoff ’Bracket’ section table.
    Returns:
        team_names (list): A list of team names.
        team_urls (list): A list of absolute Wikipedia urls corresponding to team_names.
        team_list_filtered (list): A list of team names that made it to the conference semifinals.
    """

    URL = "https://en.wikipedia.org/wiki/2021_NBA_playoffs"
    match = re.search("(https:\/\/[^:#]+\.\w+)", URL)
    BASE_URL = match[0]

    html = get_html(URL)
    soup = BeautifulSoup(html, "html.parser")
    # find bracket we are interested in
    bracket_header = soup.find(id="Bracket")
    bracket_table = bracket_header.find_next("table")
    rows = bracket_table.find_all("tr")
    # create list of teams
    team_names = []
    team_urls = []

    for i in range(1, len(rows)):
        cells = rows[i].find_all("td")
        name = re.findall(r'title=".{8}([\w ]+) season"', str(cells))
        if name != []: team_names.append(name[0])
        url = fu.find_urls(str(cells[2:4]), base_url=BASE_URL)
        if url != []: team_urls.append(url[0])

        # Filter out the teams that appear more than once, which means they made it to the conference semifinals
    team_list_filtered = [item for item, count in collections.Counter(team_names).items() if count > 1]
    team_names = list(set(team_names))
    team_urls = list(set(team_urls))

    return team_names, team_urls, team_list_filtered


def extract_players(team_url):
    """
    Extract players that played for a specific team in the NBA playoffs.
    Args:
        team_url (str): URL to the Wikipedia article of the season of a giventeam.
    Returns:
        player_names (list): A list of players names corresponding to the team whos URL was passed. semifinals.
        player_urls (list): A list of Wikipedia URLs corresponding to player_names of the team whos URL was passed.
    """

    # keep base url
    BASE_URL = "https://en.wikipedia.org"
    # get html for each page using the team url you extracted before
    html = get_html(team_url)
    # make soup
    soup = BeautifulSoup(html, "html.parser") # get the header of the Roster
    roster_header = soup.find(id="Roster") # identify table
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")
    # prepare lists for player names and urls
    player_names = []
    player_urls = []
    for i in range(0, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]
        if len(cells_text) == 7:
            rel_url = cells[2].find_next("a").attrs["href"]
            # Use e.g. regex to remove information in parenthesis following the name
            name = re.search(r'^([^()]+)',cells_text[2])
            # create urls to each player
            # need to create absolute urls combining the base and the relative url
            player_urls.append(BASE_URL + rel_url)
            player_names.append(name[0])
    return player_names , player_urls


def extract_player_statistics(player_url):
    """
    Extract player statistics for NBA player.
    Args:
        player_url (str): URL to the Wikipedia article of a player .
    Returns:
        ppg (float): Points per Game.
        bpg (float): Blocks per Game.
        rpg (float): Rebounds per Game.
    """

    # As some players have incomplete statistics/information, you can set a default score, if you want.
    ppg = 0.0
    bpg = 0.0
    rpg = 0.0
    # get html
    html = get_html(player_url)
    # make soup
    soup = BeautifulSoup(html, "html.parser")
    # find header of NBA career statistics
    nba_header = soup.find(id="NBA_career_statistics")
    # check for alternative name of header
    if nba_header is None:
        nba_header = soup.find(id="NBA")
    try:
        # find regular season header
        # You might want to check for different spellings, e.g. capitalization
        # You also want to take into account the different orders of header and table
        regular_season_header = nba_header.find_next(id="Regular_season")
        # next we should identify the table
        nba_table = regular_season_header.find_next("table")
    except:
        try:
        # table might be right after NBA career statistics header
            nba_table = nba_header.find_next("table")
        except:
            return ppg, bpg, rpg
    # find nba table header and extract rows
    table_header = nba_table.find_all("th") # YOUR CODE
    # find the columns for the different categories

    i=0
    for row in table_header:
        if re.search(r'>PPG<',str(row.contents[0])) != None:
            ppg_column = i
        if re.search(r'>BPG<',str(row.contents[0])) != None:
            bpg_column = i
        if re.search(r'>RPG<',str(row.contents[0])) != None:
            rpg_column = i
        i+=1

    rows = nba_table.find_all("tr")
    for row in rows:
        try:
            data = row.find_all("td")
            if re.search(r'2020.21', str(data)) != None:
                regex = re.compile('[^\d]*(\d{0,3}\.\d).*')
                match = regex.search(str(data[ppg_column].contents))
                tmp = match[1]
                try:
                    tmp = float(tmp)
                except ValueError:
                    tmp = 0.0
                if(tmp > ppg):
                    ppg = tmp
                match = regex.search(str(data[bpg_column].contents))
                tmp = match[1]
                try:
                    tmp = float(tmp)
                except ValueError:
                    tmp = 0.0
                if(tmp > bpg):
                    bpg = tmp
                match = regex.search(str(data[rpg_column].contents))
                tmp = match[1]
                try:
                    tmp = float(tmp)
                except ValueError:
                    tmp = 0.0
                if(tmp > rpg):
                    rpg = tmp
                """
                Some players played for more than one team during the season, only the highest ppg will be counted
                """

        except:
            continue

    return ppg, bpg, rpg


def plot_NBA_player_statistics(teams):
    """
    Extract player statistics for NBA player.
    Args:
        teams (dictionary): Dictionary with team name as the key, and a list of players as values
    Returns:
        Saves an image of the generated bar chart
    """

    color_table = {}
    colors=["lightcoral", "navajowhite", "lightgreen", "paleturquoise", "lightskyblue", "cornflowerblue", "mediumpurple", "orchid"]

    for team in teams.keys():
        color_table[team] = colors.pop()

    #Plot NBA player statistics. In this case, just PPG

    count_so_far = 0
    all_names = []
    value = "bpg"
    # iterate through each team and the
    for team, players in teams.items():
        # pick the color for the team, from the table above
        color = color_table[team]
        # collect the ppg and name of each player on the team
        # you’ll want to repeat with other stats as well
        vpg = []
        names = []
        for player in players:
            names.append(player["name"])
            vpg.append(player[value])
        # record all the names, for use later in x label
        all_names.extend(names)
        # the position of bars is shifted by the number of players so far
        x = range(count_so_far , count_so_far + len(players))
        count_so_far += len(players)
        # make bars for this team ’s players ppg ,
        # with the team name as the label
        bars = plt.bar(x, vpg, color=color, label=team, width=0.8, edgecolor="black", linewidth=1)
            # add the value as text on the bars
        plt.bar_label(bars, fontsize='small', rotation=65)
    # use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    plt.legend(title="Teams", bbox_to_anchor=(1.05, 1))
    plt.grid(False)
    plt.tight_layout()
    plt.margins(y=0.2)
    plt.title("Blocks per game")
    savename=value+".png"
    plt.savefig(savename, bbox_inches='tight')


def make_team_dict():
    """
    Support function for making a dictionary with top three players of each team
    Args:
        None
    Returns:
        ret (dictionary): A dictionary with team name as the key, and a list of the top three players as the value
    """

    tn, tu, semifinalists= extract_teams()
    teams = {}
    ret = {}
    tn.sort()
    tu.sort()

    for name in tn:
        teams[name]=[]

    y=0
    for url in tu:
        pn, pu = extract_players(url)

        i=0
        for u in pu:
            ppg, bpg, rpg = extract_player_statistics(u)
            teams[tn[y]].append({"name":pn[i], "ppg":ppg, "bpg":bpg, "rpg":rpg})
            i+=1
        y+=1


    for team, playerlist in teams.items():
        teams[team] = sorted(playerlist, key=lambda dict: dict['ppg'], reverse=True)
        teams[team] = teams[team][0:3]
        if team in semifinalists:
            ret[team] = teams[team]

    return ret


plot_NBA_player_statistics(make_team_dict())
