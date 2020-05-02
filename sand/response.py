
def error_response(resp):
    resp.status_code = 404
    resp.text = "Not found."
