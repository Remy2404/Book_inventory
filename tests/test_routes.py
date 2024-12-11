# tests/test_routes.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search_books():
    response = client.get("/books/", params={"title": "Python"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)