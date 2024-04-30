from rssched.data.access import PkgDataAccess
from rssched.io.reader import import_response


def test_import_response():
    response = import_response(PkgDataAccess.locate_response())
    print(response)
    assert len(response.schedule.fleet) == 2
