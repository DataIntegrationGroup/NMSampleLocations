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


def test_add_collabnet_well():
    response = client.post(
        "/collabnet/add",
        json={
            "well_id": 2,
            "actively_monitored": True,
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["well_id"] == 2
    assert data["actively_monitored"] is True


def test_collabnet_wells():
    response = client.get("/collabnet/location_feature_collection")
    print(response.json())
    assert response.status_code == 200


# ============= EOF =============================================
