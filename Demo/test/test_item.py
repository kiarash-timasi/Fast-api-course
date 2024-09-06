from fastapi.testclient import TestClient
from main import app  # Adjust the import path as needed

client = TestClient(app)

def test_delete_user():
    user_id = 1  # Replace with a valid user ID
    response = client.delete(f"/api/users/{user_id}/")
    assert response.status_code == 204  # Assuming successful deletion returns 204

