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
- [Basic App](basic)
- [Adding Routes](routes)
- [Templates](templates)

### Basic
```python
from sand import Sand

app = Sand()

@app.route("/")
def home(req, resp):
    resp.text = "Welcome home"

@app.route("/about")
def about(req, resp):
    resp.text = "This is what it's about"
```

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