import pytest
from sand.api import API


@pytest.fixture
def api():
    return API()


def test_route_basic(api):
    """
    Test to ensure we can add a basic route.
    :param api:
    :type API
    :return:
    """
    @api.route("/")
    def home(req, resp):
        resp.text = "Home"
