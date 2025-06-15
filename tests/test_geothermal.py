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

def test_geothermal_temperature_profile():
    """
    Test the geothermal temperature profile endpoint.
    This test should create a temperature profile and verify its creation.
    """


    # Create a sample temperature profile data


    response = client.post("/geothermal/temperature_profile", json={
        'well_id': 1,
        # "name": "Test Profile",
        # "description": "A test geothermal temperature profile",
        # "depth": 1000,
        # "temperature": 50.0
    })

    assert response.status_code == 200
    data = response.json()
    assert data['well_id'] == 1
    # assert response.json()["name"] == "Test Profile"

def test_geothermal_temperature_profile_observation():
    """
    Test the geothermal temperature profile observation endpoint.
    This test should create a temperature profile observation and verify its creation.
    """

    # Create a sample temperature profile observation data
    response = client.post("/geothermal/temperature_profile_observation", json={
        'temperature_profile_id': 1,
        'depth': 100,
        'temperature': 25.0
    })

    assert response.status_code == 200
    data = response.json()
    assert data['temperature_profile_id'] == 1
    assert data['depth'] == 100
    assert data['temperature'] == 25.0
# ============= EOF =============================================
