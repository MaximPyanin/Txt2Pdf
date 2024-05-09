import pytest
from httpx import AsyncClient,ASGITransport
from app.main import main
import os

@pytest.fixture
def get_client():
   return AsyncClient(base_url=os.getenv('TEST_URL'),transport=ASGITransport(app=main()))