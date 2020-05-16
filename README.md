![Image of Sand](docs/sand.jpg)

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
- [Basic App](Basic)
- [routes](Adding Routes)

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