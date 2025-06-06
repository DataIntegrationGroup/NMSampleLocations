from unittest import TestCase
from fastapi.testclient import TestClient
from main import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sync_engine = create_engine(
    "sqlite:///./development.db",
    echo=True,
)
from models import Base

Base.metadata.drop_all(sync_engine)
Base.metadata.create_all(sync_engine)

client = TestClient(app)


def test_get_wells():
    response = client.get("/base/well")
    assert response.status_code == 200


def test_get_locations():
    response = client.get("/base/location")
    assert response.status_code == 200


def test_get_groups():
    response = client.get("/base/group")
    assert response.status_code == 200


def test_add_location():
    response = client.post("/base/location", json={"name": "Test Location"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

    response = client.post("/base/location", json={"name": "Test Location 2"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2


def test_add_well():
    response = client.post("/base/well", json={"location_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data


def test_add_well_screen():
    response = client.post(
        "/base/wellscreen",
        json={"well_id": 1, "screen_depth_top": 10.0, "screen_depth_bottom": 20.0},
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["well_id"] == 1


def test_add_group():
    response = client.post("/base/group", json={"name": "Test Group"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Test Group"


def test_add_group_location():
    response = client.post(
        "/base/group_location", json={"group_id": 1, "location_id": 1}
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["group_id"] == 1
    assert data["location_id"] == 1


def test_add_owner():
    response = client.post("/base/owner", json={"name": "Test Owner"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Test Owner"


def test_add_contact():
    response = client.post(
        "/base/contact",
        json={
            "owner_id": 1,
            "name": "Test Contact",
            "email": "fasdfasdf",
            "phone": "1234567890",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Test Contact"
    assert data["email"] == "fasdfasdf"
