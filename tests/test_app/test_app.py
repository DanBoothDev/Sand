from sand.api import API
from sand.middleware import Middleware


def app(environ, response):
    # initialize API
    sand_app = API('tests/test_app/templates', 'tests/test_app/static')

    # add routes
    setup_routes(sand_app)

    # add exception handler
    sand_app.add_exception_handler(custom_exception_handler)

    # add middleware 
    sand_app.add_middleware(LogMiddleware)

    # return app for gunicorn
    return sand_app(environ, response)


def setup_routes(app):
    @app.route("/about")
    def about(request, response):
        response.text = "About Sand - it's small"

    @app.route("/dash")
    class Dashboard:
        def get(self, req, response):
            response.text = "Dashboard Page"

    @app.route("/")
    def home(req, resp):
        resp.body = app.template("index.html", context={"name": "Sand", "title": "Small framework"}).encode()

    @app.route("/error")
    def exception_throwing_handler(request, response):
        raise AssertionError("Some error")

def custom_exception_handler(request, response, exception_cls):
    response.text = "Oops! Something went wrong."


class LogMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)

    def process_response(self, req, res):
        print("Processing response", req.url)

