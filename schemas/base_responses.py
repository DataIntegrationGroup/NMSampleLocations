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
from schemas import ORMBaseModel


class SampleLocationResponse(ORMBaseModel):
    """
    Response schema for sample location details.
    """

    id: int
    name: str
    description: str | None = None
    # point: str  # Assuming point is a string representation of a point (e.g., "POINT(0 0)")


class WellResponse(ORMBaseModel):
    """
    Response schema for well details.
    """

    id: int
    location_id: int
    api_id: str | None = None
    ose_pod_id: str | None = None
    usgs_id: str | None = None
    # Additional fields can be added as needed


class GroupResponse(ORMBaseModel):
    """
    Response schema for group details.
    """

    id: int
    name: str
    description: str | None = None


class OwnerResponse(ORMBaseModel):
    """
    Response schema for owner details.
    """

    id: int
    name: str
    # email: str | None = None
    # phone: str | None = None


class ContactResponse(ORMBaseModel):
    """
    Response schema for contact details.
    """

    id: int
    name: str
    email: str | None = None
    phone: str | None = None


class WellScreenResponse(ORMBaseModel):
    """
    Response schema for well screen details.
    """

    id: int
    well_id: int
    screen_depth_bottom: float
    screen_depth_top: float


class GroupLocationResponse(ORMBaseModel):
    """
    Response schema for group location details.
    """

    id: int
    group_id: int
    location_id: int

class SpringResponse(ORMBaseModel):
    """
    Response schema for spring details.
    """

    id: int
    location_id: int
    description: str | None = None

# ============= EOF =============================================
