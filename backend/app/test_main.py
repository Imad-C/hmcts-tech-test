from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_task():
    response = client.post(
        "/tasks", 
        headers={"Content-Type": "application/json"}, 
        json = {
        "title": "Test Task",
        "description": "Test Task Description",
        "status": "todo",
        "due": "2025-01-01T12:00:00"
        }
        )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Test Task",
        "description": "Test Task Description",
        "status": "todo",
        "due": "2025-01-01T12:00:00"
        }
    
def test_read_tasks():
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "title": "Test Task",
        "description": "Test Task Description",
        "status": "todo",
        "due": "2025-01-01T12:00:00"
        }]
    
    