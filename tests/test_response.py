

def test_basic_response(app, client):
    """

    :param app:
    :param client:
    :return:
    """
    response_text = "42"

    @app.route("/meaning-of-life")
    def meaning_of_life(req, resp):
        resp.text = response_text

    assert client.get("http://localserver/meaning-of-life").text == response_text


def test_404_response(client):
    """
    Tests to see if the request is sent to a non-existent route
    :param client:
    :return:
    """
    response = client.get("http://localserver/done")

    assert response.status_code == 404
    assert response.text == "Not found."
