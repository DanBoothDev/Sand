from webob import Request


class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        """
        WSGI entrypoint
        """
        request = Request(environ)
        response = self.app.handle_request(request)
        return response(environ, start_response)

    def add(self, middleware_cls):
        self.app = middleware_cls(self.app)

    def handle_request(self, req):
        self.process_request(req)
        # let the app create the response
        response = self.app.handle_request(req)
        self.process_response(req, response)
        return response

    def process_request(self, req):
        # process the request in some way
        pass

    def process_response(self, req, resp):
        # process the response in some way
        pass