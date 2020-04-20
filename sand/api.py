import inspect
from os import path
from jinja2 import Environment, FileSystemLoader
from requests import Session as RequestsSession
from webob import Request, Response
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter
from sand.response import error_response


class API:
    def __init__(self, templates_dir="templates"):
        self.routes = {}
        self.exception_handler = None
        self.templates_env = Environment(loader=FileSystemLoader(path.abspath(templates_dir)))

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
        try:
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
        except Exception as e:
            if self.exception_handler is not None:
                self.exception_handler(request, response, e)
            else:
                raise e
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
        Route decorator to add a route
        """
        def wrapper(handler):
            self.add_route(path, handler)
            return handler
        return wrapper

    def add_route(self, path, handler):
        """
        Adds a route by supplying a path and handler manually
        """
        assert path not in self.routes, "Route {} already exists.".format(path)
        self.routes[path] = handler

    def test_session(self, base_url="http://localserver"):
        """
        Creates a session so we can use requests whilst testing.
        Any URL that starts with base_url will be passed to the adapter
        :param base_url: url to use as a local test server
        :return: session with a mounted WSGI adapter
        :rtype: RequestsSession
        """
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session

    def template(self, template_name, context=None):
        """
        Fetches a template with the given context
        """
        if context is None:
            # set context as default
            context = {}

        return self.templates_env.get_template(template_name).render(**context)

    def add_exception_handler(self, exception_handler):
        self.exception_handler = exception_handler