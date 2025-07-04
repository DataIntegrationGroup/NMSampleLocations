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


def test_phone_validation_fail():
    for phone in [
        "definitely not a phone",
        # "1234567890",
        # "123-456-7890",
        # "123-456-78901",
        # "123-4567-890",
        "123-456-789a",
        "123-456-7890x1234",
        "123.456.7890",
        "(123) 456-7890",
    ]:

        response = client.post(
            "/base/contact",
            json={
                "name": "Test Contact 2",
                "location_id": 1,
                "role": "Primary",
                "emails": [{"email": "fasdfasdf@gmail.com", "email_type": "Primary"}],
                "phones": [{"phone_number": phone, "phone_type": "Primary"}],
                "addresses": [
                    {
                        "address_line_1": "123 Main St",
                        "city": "Test City",
                        "state": "NM",
                        "postal_code": "87501",
                        "country": "US",
                        "address_type": "Primary",
                    }
                ],
            },
        )
        data = response.json()
        assert response.status_code == 422
        assert "detail" in data, "Expected 'detail' in response"
        assert len(data["detail"]) == 1, "Expected 1 error in response"
        detail = data["detail"][0]
        assert detail["msg"] == f"Value error, Invalid phone number. {phone}"


def test_email_validation_fail():

    for email in [
        "",
        "invalid-email",
        "invalid@domain",
        "invalid@domain.",
        "@domain.com",
    ]:
        response = client.post(
            "/base/contact",
            json={
                "name": "Test ContactX",
                "location_id": 1,
                "role": "Primary",
                "emails": [{"email": email, "email_type": "Primary"}],
                "phones": [{"phone_number": "+12345678901", "phone_type": "Primary"}],
                "addresses": [
                    {
                        "address_line_1": "123 Main St",
                        "city": "Test City",
                        "state": "NM",
                        "postal_code": "87501",
                        "country": "US",
                        "address_type": "Primary",
                    }
                ],
            },
        )
        data = response.json()
        assert response.status_code == 422
        assert "detail" in data, "Expected 'detail' in response"
        assert len(data["detail"]) == 1, "Expected 1 error in response"
        detail = data["detail"][0]
        assert detail["msg"] == f"Value error, Invalid email format. {email}"


# ============= EOF =============================================
