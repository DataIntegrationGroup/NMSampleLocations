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


def test_add_analysis_set():
    response = client.post(
        "/chemistry/analysis_set",
        json={
            "well_id": 1,
            "laboratory": "Test Lab",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["well_id"] == 1
    assert data["laboratory"] == "Test Lab"


def test_add_analysis():
    # response = client.post(
    #     "/lexicon/add",
    #     json={
    #         "term": "mg/L",
    #         "definition": "Milligrams per Liter",
    #         "category": "unit",
    #     },
    # )
    # assert response.status_code == 200
    #
    # response = client.post(
    #     "/lexicon/add",
    #     json={
    #         "term": "TDS",
    #         "definition": "Total Dissolved Solids",
    #         "category": "water_quality",
    #     },
    # )
    # assert response.status_code == 200

    response = client.post(
        "/chemistry/analysis",
        json={
            "analysis_set_id": 1,
            "value": 7.0,
            "unit": "mg/L",
            "qualifier": None,
            "analyte": "TDS",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["analysis_set_id"] == 1
    assert data["value"] == 7.0
    assert data["unit"] == "mg/L"
    assert data["qualifier"] is None
    assert data["analyte"] == "TDS"


# ============= EOF =============================================
