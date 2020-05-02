import pytest
from sand import Sand


@pytest.fixture
def app():
    return Sand()


@pytest.fixture
def client(app):
    return app.test_session()
