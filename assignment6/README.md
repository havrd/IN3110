# Assignment 6


## Dependencies
All packages can be installed using `pip`.

See requirements in `requirements.txt`

## 6.1 Cases over time plotter
The script `webvisualization_plots.py` includes one public function `plot_reported_cases_per_million(countries=None, start=None, end=None)`.

When run as a script the following default values are used:
- countries: The 6 countries with the highest number of cases per million at the last current date available in the timeframe chosen.
- start: 2020-02-24 00:00:00
- end: 2021-11-23 00:00:00

How to run examples:
```bash
python3 webvisualization_plots.py
```

## 6.2 Becoming a web app developer using FastAPI
The script `webvisualization.py` hosts a web app that displays the graph from 5.1.

When run as a script the program displays a graph using default values on http://localhost:8080

How to run examples:
```bash
python3 webvisualization.py
```
## 6.3 Interactive visualization: Upgrading to pro-level
Not implemented

## 6.5 Documentation and help page
Not implemented
