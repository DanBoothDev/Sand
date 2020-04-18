import inspect
from webob import Request, Response
from sand.response import error_response


class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        """
        WSGI callable
        :param environ          request info including CGI env vars
        :param start_response   used to begin the HTTP response
        :return WSGI compatible formatted response
        """
        request = Request(environ)
        response = self._request_handler(request)

        return response(environ, start_response)
    
    def _request_handler(self, request):
        """
        Request handler takes the inbound request and transforms 
        :param request      inbound request
        :return response    a formatted webob response
        """
        response = Response()

        handler = self.get_route_handler(request.path)
        if handler is not None:
            if inspect.isclass(handler):
                # check to see if the class supports the requested method i.e. GET/POST
                handler = getattr(handler(), request.method.lower(), None)
                if handler is None:
                    raise AttributeError("Unsupported request method", request.method)

            # update response with associated handler
            handler(request, response)
        else:
            # unable to find handler - display error
            error_response(response)
        return response

    def get_route_handler(self, request_path):
        """
        Gets the route handler if applicable
        :param request_path     path to be routed
        :return route handler if available else None
        """
        if request_path in self.routes.keys():
            return self.routes.get(request_path)
        return None

    def route(self, path):
        """
        Route decorator
        """
        assert path not in self.routes, "Route {} already exists.".format(path)

        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper
