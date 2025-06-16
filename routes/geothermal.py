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
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import get_db_session, adder
from models.geothermal import (
    GeothermalTemperatureProfile,
    GeothermalTemperatureProfileObservation, GeothermalBottomHoleTemperature,
)
from schemas.geothermal import (
    CreateTemperatureProfile,
    CreateTemperatureProfileObservation, CreateBottomHoleTemperature,
)

router = APIRouter(prefix="/geothermal", tags=["geothermal"])


@router.post("/temperature_profile")
async def add_temperature_profile(
    temperature_profile_data: CreateTemperatureProfile,
    session: Session = Depends(get_db_session),
):
    """
    Add a new temperature profile.
    """
    return adder(session, GeothermalTemperatureProfile, temperature_profile_data)


@router.post("/temperature_profile_observation")
async def add_temperature_profile_observation(
    temperature_profile_observation_data: CreateTemperatureProfileObservation,
    session: Session = Depends(get_db_session),
):
    """
    Add a new temperature profile observation.
    """
    return adder(
        session,
        GeothermalTemperatureProfileObservation,
        temperature_profile_observation_data,
    )

@router.post('/bottom_hole_temperature')
async def add_bottom_hole_temperature(
    bottom_hole_temperature_data: CreateBottomHoleTemperature,
    session: Session = Depends(get_db_session),
):
    """
    Add a new bottom hole temperature.
    """
    return adder(
        session,
        GeothermalBottomHoleTemperature,  # Assuming this is the correct model
        bottom_hole_temperature_data,
    )
# ============= EOF =============================================
