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


def test_well_form():
    payload = {
        "location": {"point": "POINT(-105.0 40.0)"},
        "owner": {
            "name": "John Doe",
            "contact": [
                {"name": "John Doe", "phone": "123-456-7890", "email": "foo@gmail.com"},
                {
                    "name": "Jane Doe",
                    "phone": "913-356-7890",
                    "email": "jane@gmail.com",
                },
            ],
        },
    }

    response = client.post("/form/well", json=payload)
    assert response.status_code == 200
    data = response.json()
    location = data.get("location", None)
    assert location is not None
    assert location.get("point") == 'POINT(-105.0 40.0)'

    owner = data.get("owner", None)
    assert owner is not None
    assert owner.get("name") == "John Doe"

    contacts = owner.get("contacts", [])
    assert len(contacts) == 2
    assert contacts[0].get("name") == "John Doe"
    assert contacts[0].get("phone") == "123-456-7890"

    # Ensure the second contact is also correct
    assert contacts[1].get("name") == "Jane Doe"
    assert contacts[1].get("phone") == "913-356-7890"


# ============= EOF =============================================
