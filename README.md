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

