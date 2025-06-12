# ===============================================================================
# Copyright 2025 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

from tests import client


def test_query_eq_true():
    response = client.get(
        "/base/location",
        params={
            "query": "visible eq true",
        },
    )
    assert response.status_code == 200
    data = response.json()
    items = data["items"]
    assert len(items) == 1


def test_query_eq_false():
    response = client.get(
        "/base/location",
        params={
            "query": "visible eq false",
        },
    )
    assert response.status_code == 200
    data = response.json()
    items = data["items"]
    assert len(items) == 2


def test_query_nested_eq():
    response = client.get(
        "/base/location",
        params={
            "query": "well.api_id eq '1001-0001'",
        },
    )
    assert response.status_code == 200
    data = response.json()
    items = data["items"]
    assert len(items) == 1
    assert items[0]["name"] == "Test Location 1"  # Assuming this is the expected name


def test_query_nested_ne():
    response = client.get(
        "/base/location",
        params={
            "query": "well.api_id ne '1001-0001'",
        },
    )
    assert response.status_code == 200
    data = response.json()
    items = data["items"]
    assert len(items) == 2  # Assuming there are two locations not matching the API ID
    assert all(
        item["name"] != "Test Location 1" for item in items
    )  # Ensure none match the excluded ID


def test_query_nested_like():
    response = client.get(
        "/base/location",
        params={
            "query": "well.api_id like '1001-%'",
        },
    )
    assert response.status_code == 200
    data = response.json()
    items = data["items"]
    assert len(items) == 2
    assert items[0]["name"] == "Test Location 1"
    assert items[1]["name"] == "Test Location 2"

    # assert len(items) > 0  # Assuming there are locations with well names containing 'Test'
    # assert all("Test" in item["well"]["name"] for item in items)  # Ensure all returned wells match the condition


# ============= EOF =============================================
