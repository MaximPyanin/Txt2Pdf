import pytest
from httpx import AsyncClient
from app.main import main

@pytest.fixture
def get_client():
   return AsyncClient(base_url='http://localhost:8000',app=main())