# SQLPlot
Command line tool for plotting columns in SQL databases

# Installation
Download the package and go into the root directory of the pacakge

```bash
pip install -r requirements.txt --user
pip instlal . --user
```

# Usage
If we have a SQLite database **statistics.db** with table named **heights** the following layout,

| Age | Height |
| --- | ------ |
| 4 | 80 |
| 5 | 90  |
| 7 | 130 |
| 10 | 145 |
| 13  | 150 | 
| 15  | 160 |
| 18 | 175 |

The content can easily be plotted by
```bash
sqlplot sqlite:///heights.db 'select Age,Height from heights'
```
