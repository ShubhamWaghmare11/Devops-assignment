import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"  # in-memory DB for tests
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Seed some test users
            db.session.add_all([
                User(name="TestUser1"),
                User(name="TestUser2")
            ])
            db.session.commit()
        yield client

def test_get_users(client):
    response = client.get("/api/data")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["name"] == "TestUser1"
