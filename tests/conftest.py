import pytest
from sand.api import API


@pytest.fixture
def app():
    return API()
