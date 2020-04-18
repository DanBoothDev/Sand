from sand.api import API


def app(environ, response):
    # initialize API
    sand_app = API()

    # add routes
    setup_routes(sand_app)

    # return app for gunicorn
    return sand_app(environ, response)


def setup_routes(app):
    @app.route("/")
    def home(request, response):
        response.text = "Welcome home"

    @app.route("/about")
    def about(request, response):
        response.text = "About Sand - it's small"

    @app.route("/dash")
    class Dashboard:
        def get(self, req, response):
            response.text = "Dashboard Page"