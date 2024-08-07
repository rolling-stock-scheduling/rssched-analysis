import time
from pathlib import Path
from typing import Annotated

import typer
from typer import Argument, echo

from rssched.io.reader import import_response
from rssched.visualization.plot import generate_plots

app = typer.Typer()


@app.command()
def main(source: Annotated[Path, Argument()]):
    echo(f"Render visualization(s): {source}")
    response = import_response(source)
    for fig in generate_plots(response, source.stem):
        fig.show()
        time.sleep(0.5)


if __name__ == "__main__":
    app()
