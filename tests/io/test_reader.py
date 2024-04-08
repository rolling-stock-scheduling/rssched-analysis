from rssched.data.access import PkgDataAccess
from rssched.io.reader import import_response


def test_import_response():
    response = import_response(PkgDataAccess.locate_response())
    assert len(response.schedule) == 3
