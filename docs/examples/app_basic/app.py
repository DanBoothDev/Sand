from sand import Sand

app = Sand()


@app.route("/")
def home(req, resp):
    resp.text = "Welcome home"


@app.route("/about")
def about(req, resp):
    resp.text = "This is what it's about"
