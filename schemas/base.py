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
from datetime import datetime

from pydantic import field_validator, model_validator

from schemas import ORMBaseModel


class CreateLocation(ORMBaseModel):
    """
    Schema for creating a sample location.
    """

    name: str
    description: str | None = None
    point: str = "POINT(0 0)"  # Default to a point at the origin


class CreateWell(ORMBaseModel):
    """
    Schema for creating a well.
    """

    location_id: int


class CreateScreenWell(ORMBaseModel):
    """
    Schema for creating a well screen.
    """

    well_id: int
    screen_depth_bottom: float
    screen_depth_top: float

    # validate that screen depth bottom is greater than top
    @model_validator(mode="after")
    def check_depths(self):
        if self.screen_depth_bottom < self.screen_depth_top:
            raise ValueError(
                "screen_depth_bottom must be greater than screen_depth_top"
            )
        return self


class CreateGroup(ORMBaseModel):
    """
    Schema for creating a group.
    """

    name: str


class CreateGroupLocation(ORMBaseModel):
    """
    Schema for creating a group location.
    """

    group_id: int
    location_id: int


class CreateOwner(ORMBaseModel):
    """
    Schema for creating an owner.
    """

    name: str
    description: str | None = None


class CreateContact(ORMBaseModel):
    """
    Schema for creating a contact.
    """

    owner_id: int

    name: str | None = None
    description: str | None = None
    email: str | None = None
    phone: str | None = None


class CreateSpring(ORMBaseModel):
    """
    Schema for creating a spring.
    """

    location_id: int


class BaseRecord(ORMBaseModel):
    """
    Base schema for records that have an ID.
    """

    id: int
    created_at: datetime


class GetLocation(BaseRecord):
    """
    Schema for a sample location.
    """

    name: str | None = None
    description: str | None = None


class GetWell(BaseRecord):
    """
    Schema for a well.
    """

    id: int


class GetGroup(BaseRecord):
    """
    Schema for a group.
    """

    id: int
    # name: str | None = None
    # description: str | None = None


# ============= EOF =============================================
