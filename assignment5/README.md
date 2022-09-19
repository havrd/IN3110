# Assignment 5


## Dependencies
All packages can be installed using `pip`.

See requirements in `requirements.txt`

## 5.1 Sending URL requests
The script `requesting_urls.py` includes one public function `get_html(url, params, output)`.

When run as a script the following URLs are requested without parameters:
- https://en.wikipedia.org/wiki/Studio_Ghibli
- https://en.wikipedia.org/wiki/Star_Wars

and https://en.wikipedia.org/w/index.php is requested using the following parameters:
- title=Main Page and action=info

The output (URL and HTML as .txt files) of these examples can be found in the `requesting_urls` folder.

How to run examples:
```bash
python3 requesting_urls.py
```

## 5.2 Regex for filtering URLs
The script `filter_urls.py` includes two public functions `find_urls(html_str, base_url, output)` and `find_articles(html_str, base_url, output)`.

When run as a script the following URLs are given to `find_articles` with base="https://en.wikipedia.org":
- https://en.wikipedia.org/wiki/Nobel_Prize
- https://en.wikipedia.org/wiki/Bundesliga
- https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup

The output (all URLs and only Wikipedia articles as .txt files) of these examples can be found in the `filter_urls` folder.

How to run examples:
```bash
python3 filter_urls.py
```


## 5.4 Filtering datetime objects using soup
The script `time_planner.py` includes two public functions `extract_events(url)` and `create_betting_slip(events, save_as)`.

When run as a script "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup" is used as an example.

The output (a betting slip as .md file) of this example can be found in the `datetime_filter` folder.

How to run examples:
```bash
python3 time_planner.py
```

## 5.5 NBA Player Statistics Season 2020/2021
The script `fetch_player_statistics.py` includes two public functions `plot_NBA_player_statistics(teams)` and `make_team_dict()`.

When run as a script "https://en.wikipedia.org/wiki/2021_NBA_playoffs" is used as an example.

The output (three plots of the players over the points/blocks/rebounds per game) of this example can be found in the `NBA_player_statistics` folder.

How to run examples:
```bash
python3 fetch_player_statistics.py
```

## 5.6 Challenge - Wiki Race with URLs
The script `wiki_race_challenge.py` includes one public function `find_path(start, end)`.

When run as a script start="https://en.wikipedia.org/wiki/Nobel_Prize" and end="https://en.wikipedia.org/wiki/Array_data_structure".

The output (txt-file with shortest path) of this example can be found in the `wiki_race_challenge` folder.

How to run examples:
```bash
python3 wiki_race_challenge.py
```
