from fastapi.testclient import TestClient
from main import app
from models import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

client = TestClient(app)


#  ADD tests ======================================================
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
    response = client.post("/base/well", json={"location_id": 1,
                                               'api_id': '1001-0001',
                                               'ose_pod_id': 'RA-0001',})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data

    response = client.post("/base/well", json={"location_id": 2,
                                               'api_id': '1001-0002',
                                               'ose_pod_id': 'RA-0002',})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data

def test_add_spring():
    response = client.post("/base/spring", json={"location_id": 1})
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


# GET tests ======================================================
def test_get_springs():
    response = client.get("/base/spring")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_wells():
    response = client.get("/base/well")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_locations():
    response = client.get("/base/location")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_groups():
    response = client.get("/base/group")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_owners():
    response = client.get("/base/owner")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_contacts():
    response = client.get("/base/contact")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_well_screens():
    response = client.get("/base/wellscreen")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_group_locations():
    response = client.get("/base/group_location")
    assert response.status_code == 200
    assert len(response.json()) > 0

# test item retrieval via filter ===========================================
def test_item_get_well_filter():
    response = client.get("/base/well", params={"api_id": '1001-0002'})
    assert response.status_code == 200
    data = response.json()
    assert len(data) ==1
    item = data[0]
    assert 'api_id' in item
    assert item["api_id"] == '1001-0002'

# Test item retrieval ======================================================
def test_item_get_spring():
    response = client.get("/base/spring/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["location_id"] == 1

def test_item_get_owner():
    response = client.get("/base/owner/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Test Owner"


def test_item_get_location():
    response = client.get("/base/location/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Test Location"


def test_item_get_group():
    response = client.get("/base/group/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Test Group"


def test_item_get_wells():
    response = client.get("/base/well/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["location_id"] == 1


def test_item_get_well_screens():
    response = client.get("/base/wellscreen/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["well_id"] == 1
    assert data["screen_depth_top"] == 10.0
    assert data["screen_depth_bottom"] == 20.0


def test_item_get_group_locations():
    response = client.get("/base/group_location/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["group_id"] == 1
    assert data["location_id"] == 1


def test_item_get_contact():
    response = client.get("/base/contact/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Test Contact"
    assert data["email"] == "fasdfasdf"
    assert data["phone"] == "1234567890"
