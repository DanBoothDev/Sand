
def error_response(response):
    response.status_code = 404
    response.text = "Not found."
