# RSSched Output Analysis and Visualization

Analysis and visualization of results from the scheduler service. Part of the Innosuisse project
Rolling Stock Scheduling (RSSched) by SBB and ETH Zurich.

## Setup

1) install poetry: https://python-poetry.org/docs/

2) run:

```sh
poetry install
```

## Gantt

Visualize scheduler output as a Gantt chart:

```sh
poetry run rssched-gantt rssched/data/output_small_test_input.json
