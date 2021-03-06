from datetime import datetime
from sand import Sand
from sand.middleware import Middleware


def app(environ, response):
    # initialize API
    sand_app = Sand('./templates', './static')

    # add routes
    setup_routes(sand_app)

    # add exception handler
    sand_app.add_exception_handler(custom_exception_handler)

    # add middleware 
    sand_app.add_middleware(LogMiddleware)

    # return WSGI compatible app
    return sand_app(environ, response)


def setup_routes(app):
    @app.route("/about")
    def about(req, resp):
        resp.text = "About Sand - it's small"

    @app.route("/dash")
    class Dashboard:
        def get(self, req, resp):
            resp.text = "Dashboard Page"

    @app.route("/")
    def home(req, resp):
        context = {
            "name": "Sand",
            "title": "Small framework"
        }
        resp.body = app.template("index.html", context).encode()

    @app.route("/error")
    def exception_throwing_handler(req, resp):
        raise AssertionError("Some error")


def custom_exception_handler(req, resp, exc_class):
    resp.text = "Oops! Something went wrong."


class LogMiddleware(Middleware):
    def process_request(self, req):
        print("[{}] RX: {} {} {} - {}".format(self._get_utc_now(), req.client_addr, req.method, req.path, req.user_agent))

    def process_response(self, req, resp):
        print("[{}] TX: {} {} {} {} - {}".format(self._get_utc_now(), req.client_addr, req.method, req.path, resp.status, req.user_agent))

    def _get_utc_now(self):
        return datetime.utcnow().isoformat()
