![Image of Sand](docs/img/sand.jpg)

# Sand

Sand is small Python web framework.


## Features
- WSGI compatible
- Routing via decorator or paramaters  
- Use class based handlers
- Template support (jinja)
- Static file
- Custom exception handling
- Middleware

## Installing
```
$(venv) pip install -r requirements.txt
```

## Running
```
gunicorn app:app
```

## Testing
```
python setup.py test
```

## Usage
- [App](app)
- [Adding Routes](routes)
- [Templates](templates)
- [Static Files](static-files)
- [Exception Handlers](exceptions-handlers)
- [Middleware](middleware)


### App
For example apps see:
- [Basic App](docs/examples/app_basic)
- [Advanced App](docs/examples/app_advanced)
- [Sandcastle](https://github.com/DanBoothDev/Sandcastle) an example app using the Sand framework

### Routes
```python
from sand import Sand

app = Sand()

# using decorators
@app.route("/")
def home(req, resp):
    resp.text = "Welcome home"

# using parameters
def about(req, resp):
    resp.text = "This is what it's about"

app.add_route("/about", about)
```

### Templates
When initialising Sand, the default template directory is `/templates`. To use a different directory, use `templates_dir`

```python
from sand import Sand

app = Sand(templates_dir='path/to/templates')

@app.route("/")
def home(req, resp):
    context = {
        "name": "Sand",
        "title": "Home"
    }
    resp.body = app.template("index.html", context).encode()
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>The name of the framework is {{ name }}</h1>
</body>
</html>
```

### Static Files
Like templates, when initializing sand, the default static directory is `/static`. To use a different directory, use `static_dir`

```python
from sand import Sand

app = Sand(static_dir='path/to/static')

...
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link href="/static/main.css" type="text/css" rel="stylesheet">
</head>
<body>
    <h1>The name of the framework is {{ name }}</h1>
</body>
</html>
```
### Exception Handlers
```python
from sand import Sand

app = Sand()

def custom_exception_handler(req, resp, exc_class):
    resp.text = "Oops! Something went wrong."

app.add_exception_handler(custom_exception_handler)
...
```

### Middleware
```python
from sand import Sand
from sand.middleware import Middleware

app = Sand()


class LogMiddleware(Middleware):
    def process_request(self, req):
        print("RX: {} {} {} - {}".format(req.client_addr, req.method, req.path, req.user_agent))

    def process_response(self, req, resp):
        print("TX: {} {} {} {} - {}".format(req.client_addr, req.method, req.path, resp.status, req.user_agent))

app.add_middleware(LogMiddleware)
...
```