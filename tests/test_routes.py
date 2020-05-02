import pytest


def test_route_basic_decorator(app):
    """
    Test to ensure we can add a basic route.
    """
    @app.route("/")
    def home(req, resp):
        resp.text = "Home"


def test_route_manual(app, client):
    """
    Test to ensure we can add a route by supplying the path and handler
    """
    response_text = "Manually add a route"

    def manual_handler(req, resp):
        resp.text = response_text

    app.add_route("/manual_route", manual_handler)

    assert client.get("http://localserver/manual_route").text == response_text


def test_route_duplicate(app):
    """
    Test to ensure we can't add duplicate routes.
    :param app:
    :return:
    """
    @app.route("/")
    def home(req, resp):
        resp.text = "Home"

    with pytest.raises(AssertionError):
        @app.route("/")
        def home2(req, resp):
            resp.text = "Home"
