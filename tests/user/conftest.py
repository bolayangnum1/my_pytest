import pytest
import requests
from configuration import SERVICE_URL_USER_API


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL_USER_API)
    return response
