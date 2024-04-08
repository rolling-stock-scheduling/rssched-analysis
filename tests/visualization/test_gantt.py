from rssched.data.access import PkgDataAccess
from rssched.io.reader import import_response
from rssched.visualization.gantt import respone_to_gantt


def test_response_to_gant():
    response = import_response(PkgDataAccess.locate_response())
    respone_to_gantt(response, "Rolling stock schedule")
