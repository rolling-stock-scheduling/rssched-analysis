from rssched.data.access import PkgDataAccess
from rssched.io.reader import import_request, import_response


def test_import_request():
    request = import_request(PkgDataAccess.locate_request())
    print(request)
    assert len(request.vehicle_types) == 2
    assert len(request.routes) == 2


def test_import_response():
    response = import_response(PkgDataAccess.locate_response())
    print(response)
    assert len(response.schedule.fleet) == 2
