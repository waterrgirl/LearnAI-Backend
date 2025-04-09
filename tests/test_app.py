import pytest
from app import create_app

@pytest.fixture
def client():
    flask_app = create_app()
    flask_app.config['TESTING'] = True
    return flask_app.test_client()

def test_index_route(client):
    resp = client.get("/")
    assert resp.status_code == 200
