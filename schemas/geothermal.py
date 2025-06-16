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
from pydantic import BaseModel


class CreateTemperatureProfile(BaseModel):
    """
    Pydantic model for creating a temperature profile.
    This model can be extended to include additional fields as needed.
    """

    well_id: int


class CreateTemperatureProfileObservation(BaseModel):
    """
    Pydantic model for creating a temperature profile observation.
    This model can be extended to include additional fields as needed.
    """

    temperature_profile_id: int
    depth: float
    depth_unit: str = "ft"  # Assuming depth unit is a string (e.g., 'm', 'ft')
    temperature: float
    temperature_unit: str = (
        "F"  # Assuming temperature unit is a string (e.g., 'C', 'F')
    )


class CreateBottomHoleTemperature(BaseModel):
    """
    Pydantic model for creating a bottom hole temperature observation.
    This model can be extended to include additional fields as needed.
    """

    well_id: int
    # depth: float
    temperature: float
    # depth_unit: str  # Assuming depth unit is a string (e.g., 'm', 'ft')
    temperature_unit: str = (
        "F"  # Assuming temperature unit is a string (e.g., 'C', 'F')
    )


# ============= EOF =============================================
