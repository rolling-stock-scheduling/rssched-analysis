from rssched.data.access import PkgDataAccess
from rssched.io.reader import import_response
from rssched.visualization.gantt import response_to_gantt


def test_response_to_gant():
    response = import_response(PkgDataAccess.locate_response())
    figs = response_to_gantt(response, "test_instance")
    assert len(figs) == 2
