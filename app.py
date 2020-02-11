from sand.api import API


def test_app():
    # initialize API
    app = API()

    # add routes
    setup_routes(app)

    # return app for gunicorn
    return app

def setup_routes(app):
    @app.route("/")
    def home(request, response):
        response.text = "Welcome home"

    @app.route("/about")
    def about(request, response):
        response.text = "About Sand - it's small"
