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

from models import get_db
from models.base import Well, SampleLocation, Group
from schemas.base import GetWell,  GetLocation, CreateLocation, CreateWell, CreateGroup

router = APIRouter(
    prefix="/base",
)

@router.post('/location',
             response_model=GetLocation,
             summary='Create a new sample location')
async def create_location(location_data: CreateLocation, db: Session = Depends(get_db)):
    """
    Create a new sample location in the database.
    """
    # Placeholder for actual database insertion logic
    #return {"message": "This endpoint will create a new sample location.", "data": location_data}

    sample_location = SampleLocation(**location_data.model_dump())
    db.add(sample_location)
    await db.commit()
    return sample_location


@router.post('/well',
             response_model=GetWell,
             summary='Create a new well')
async def create_well(well_data: CreateWell, db: Session = Depends(get_db)):
    """
    Create a new well in the database.
    """
    # Placeholder for actual database insertion logic
    #return {"message": "This endpoint will create a new well.", "data": well_data}
    well = Well(**well_data.model_dump())
    db.add(well)
    await db.commit()
    return well

@router.post('/group',
                summary='Create a new group')
async def create_group(group_data: CreateGroup, db: Session = Depends(get_db)):
    """
    Create a new group in the database.
    """
    # Placeholder for actual database insertion logic
    # return {"message": "This endpoint will create a new group.", "data": group_data}
    group = Group(**group_data.model_dump())
    db.add(group)
    await db.commit()
    return group

# ==== Get ============================================
@router.get("/location", summary="Get all wells")
async def get_location(db: Session = Depends(get_db)):
    """
    Retrieve all wells from the database.
    """
    # Placeholder for actual database retrieval logic
    # return {"message": "This endpoint will return all wells."}
    sql = select(SampleLocation)
    result = await db.execute(sql)
    return result


@router.get("/well", summary="Get all wells")
async def get_wells(db: Session = Depends(get_db)):
    """
    Retrieve all wells from the database.
    """
    # Placeholder for actual database retrieval logic
    # return {"message": "This endpoint will return all wells."}
    sql = select(Well)
    result = await db.execute(sql)
    return result


@router.get('/group', summary="Get groups")
async def get_groups(db: Session = Depends(get_db)):
    """
    Retrieve all groups from the database.
    """
    sql = select(Group)
    result = await db.execute(sql)
    return result.all()



# ============= EOF =============================================
