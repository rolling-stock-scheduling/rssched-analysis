# RSSched Output Analysis and Visualization

Analysis and visualization of results from the scheduler service. Part of the Innosuisse project
Rolling Stock Scheduling (RSSched) by SBB and ETH Zurich.

## Setup

1. install poetry a package manager for python: https://python-poetry.org/docs/

2. install the dependencies for this project via:
   
   ```sh
   poetry install
   ```

## Plots

Visualize scheduler output:

```sh
poetry run rssched-plot rssched/data/output_small_test_input.json
```

---

© 2024 SBB CFF FFS. Licensed under MIT.
