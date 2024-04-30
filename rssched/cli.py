from pathlib import Path
from typing import Annotated

import typer
from typer import Argument, echo

from rssched.io.reader import import_response
from rssched.visualization.gantt import response_to_gantt

app = typer.Typer()


@app.command()
def main(source: Annotated[Path, Argument()]):
    echo(f"Render visualization(s): {source}")
    response = import_response(source)
    for fig in response_to_gantt(response, source.stem):
        fig.show()


if __name__ == "__main__":
    app()
