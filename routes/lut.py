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
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import get_db_session, adder
from models.base import SampleLocation

from models.lut import LUT_Well_Type, LU_Formation_Zone
from schemas.lut_create import CreateWellType, CreateFormationZone
from schemas.lut_responses import WellTypeResponse, FormationZoneResponse

router = APIRouter(
    prefix="/lut",
)


# Adders
@router.post("/well_type", response_model=WellTypeResponse)
def add_well_type(
    well_type: CreateWellType, session: Session = Depends(get_db_session)
):
    """
    Add a new well type to the database.
    """
    return adder(session, LUT_Well_Type, well_type)


@router.post("/formation_zone", response_model=FormationZoneResponse)
def add_formation_zone(
    formation_zone: CreateFormationZone, session: Session = Depends(get_db_session)
):
    """
    Add a new formation zone to the database.
    """
    return adder(session, LU_Formation_Zone, formation_zone)


# Getters
@router.get("/well_types", response_model=list[WellTypeResponse])
def get_well_types(session: Session = Depends(get_db_session)):
    """
    Retrieve all well types from the database.
    """
    sql = select(LUT_Well_Type)
    return session.scalars(sql).all()

    # well_types = db.query(LUT_Well_Type).all()
    # return [WellTypeResponse.from_orm(wt) for wt in well_types]


# ============= EOF =============================================
