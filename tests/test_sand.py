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


def test_route_duplicate(api):
    """
    Test to ensure we can't add duplicate routes.
    :param api:
    :return:
    """
    @api.route("/")
    def home(req, resp):
        resp.text = "Home"

    with pytest.raises(AssertionError):
        @api.route("/")
        def home2(req, resp):
            resp.text = "Home"
