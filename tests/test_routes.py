import pytest


def test_route_basic(app):
    """
    Test to ensure we can add a basic route.
    :param api:
    :type API
    :return:
    """
    @app.route("/")
    def home(req, resp):
        resp.text = "Home"


def test_route_duplicate(app):
    """
    Test to ensure we can't add duplicate routes.
    :param api:
    :return:
    """
    @app.route("/")
    def home(req, resp):
        resp.text = "Home"

    with pytest.raises(AssertionError):
        @app.route("/")
        def home2(req, resp):
            resp.text = "Home"
