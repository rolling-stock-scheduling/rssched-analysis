from rssched.data.access import PkgDataAccess
from rssched.io.reader import import_response
from rssched.visualization.plot import generate_plots


def test_generate_plots():
    response = import_response(PkgDataAccess.locate_response())
    figs = generate_plots(response, "test_instance")
    assert len(figs) == 4
