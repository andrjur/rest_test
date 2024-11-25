def test_create_task():
    response = client.post("/tasks", json={"title": "Тестовая задача"})
    assert response.status_code == 201