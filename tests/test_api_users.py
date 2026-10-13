import pytest
import requests

BASE_URL = "https://reqres.in/api"

@pytest.mark.api
@pytest.mark.smoke
def test_get_users_list_status_and_schema():
    """Verify GET /users returns 200 and paginated user objects."""
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0

    user = data["data"][0]
    assert "id" in user
    assert "email" in user
    assert "@" in user["email"]

@pytest.mark.api
def test_create_user_post_endpoint():
    """Verify POST /users returns 201 Created and echoes input payload."""
    payload = {
        "name": "Brooklin",
        "job": "QA Automation Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201

    result = response.json()
    assert result["name"] == payload["name"]
    assert result["job"] == payload["job"]
    assert "id" in result
