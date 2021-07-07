"""
Author: Abdur Rehman
"""
import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all():

    response = client.get("/")
    assert response.status_code == 200


def test_get_one():
    response = client.get("/?task_id=1")
    assert response.status_code == 200


def test_create_new():
    data = {"title": "test case", "description": "test case description"}
    response = client.post("/", data=json.dumps(data),
                           headers={"Content-Type": "application/json"})
    assert response.status_code == 200


def test_delete():
    response = client.get("/?task_id=1")
    assert response.status_code == 200
