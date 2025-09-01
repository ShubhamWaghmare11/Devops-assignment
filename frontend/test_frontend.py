import pytest
from frontend import app
from unittest.mock import patch
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_success(client):
    # Mock requests.get to simulate backend response
    mock_data = [{"id": 1, "name": "Shubham"}]
    with patch("frontend.requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_data
        response = client.get("/")
        assert response.status_code == 200
        assert b"Shubham" in response.data  # HTML contains user name

def test_index_backend_failure(client):
    # Simulate backend failure 
    
    with patch("frontend.requests.get") as mock_get:
        mock_get.side_effect = Exception("Backend down")
        response = client.get("/")
        assert response.status_code == 200
        assert b"Backend down" in response.data
