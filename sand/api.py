
class API:
    def __call__(self, environ, start_response):
        response_body = b"Welcome to Sand!"
        status = "200 OK"
        start_response(status, headers=[])
        return iter([response_body])
