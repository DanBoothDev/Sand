![Image of Sand](docs/sand.jpg)

# Sand

Sand is small Python web framework.

### Installing
```
$(venv) pip install -r requirements.txt
```

## Running
```
gunicorn tests.test_app.test_app:app
```

## Testing
```
python setup.py test
```

## Authors

* **Daniel Booth** - [DanBoothDev](https://github.com/DanBoothDev)


## Dependencies
- [Gunicorn](https://pypi.org/project/gunicorn/) - WSGI HTTP Server for UNIX
- [WebOb](https://pypi.org/project/WebOb/) - requests and response helper
- [WhiteNoise](https://pypi.org/project/whitenoise) - static file serving
