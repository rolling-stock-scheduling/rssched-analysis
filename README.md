# RSSched Output Analysis and Visualization

Analysis and visualization of results from the scheduler service. Part of the Innosuisse project
Rolling Stock Scheduling (RSSched) by SBB and ETH Zurich.

# Usage

To get started with the whole RSSched project, have a look at this [step-by-step instruction](https://github.com/rolling-stock-scheduling/.github/blob/main/getting_started.md).

## Setup

1. install poetry a package manager for python: https://python-poetry.org/docs/

2. install the dependencies for this project via:
   
   ```sh
   poetry install
   ```

## Plots

Visualize scheduler output:

```sh
poetry run rssched-plot your/schedule.json
```

---

© 2024 SBB CFF FFS. Licensed under MIT.
