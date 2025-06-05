from unittest import TestCase
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_wells():

    response = client.get("/base/wells")
    data = response.json()
    assert response.status_code == 200


    # assert "message" in data
    # assert data["message"] == "This endpoint will return all wells."
# class TestBase(TestCase):
#     def test_get_wells(self):
#         client = TestClient(app)
#
#         response = client.get("/base/wells")
#         data = response.json()
#         assert response.status_code == 200