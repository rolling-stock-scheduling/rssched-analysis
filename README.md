# RSSched Output Analysis and Visualization

Analysis and visualization of results from the rolling stock scheduling.

## Setup

1) install poetry: https://python-poetry.org/docs/

2) run:

```sh
poetry install
```

## Gantt

Visualize scheduler output as a Gantt chart:

```sh
poetry run rssched-gantt rolling_stock_scheduling/data/small_test_output.json
