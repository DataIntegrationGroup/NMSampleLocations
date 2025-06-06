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
from models.base import Well, SampleLocation, Group, GroupLocation, Owner, Contact, WellScreen
from schemas.base import GetWell, GetLocation, CreateLocation, CreateWell, CreateGroup, CreateGroupLocation, \
    CreateOwner, CreateContact, CreateScreenWell

router = APIRouter(
    prefix="/base",
)


async def adder(db, table, model):
    """
    Helper function to add a new record to the database.
    """
    obj = table(**model.model_dump())
    db.add(obj)
    await db.commit()
    return obj

@router.post(
    "/location", response_model=GetLocation, summary="Create a new sample location"
)
async def create_location(location_data: CreateLocation, db: Session = Depends(get_db)):
    """
    Create a new sample location in the database.
    """
    return await adder(db, SampleLocation, location_data)


@router.post("/well", response_model=GetWell, summary="Create a new well")
async def create_well(well_data: CreateWell, db: Session = Depends(get_db)):
    """
    Create a new well in the database.
    """
    return await adder(db, Well, well_data)

@router.post("/wellscreen", summary="Create a new well screen")
async def create_wellscreen(well_screen_data: CreateScreenWell, db: Session = Depends(get_db)):
    """
    Create a new well screen in the database.
    """
    return await adder(db, WellScreen, well_screen_data)

@router.post("/group", summary="Create a new group")
async def create_group(group_data: CreateGroup, db: Session = Depends(get_db)):
    """
    Create a new group in the database.
    """
    return await adder(db, Group, group_data)


@router.post("/group_location", summary="Create a new group location")
async def create_group_location(group_location_data: CreateGroupLocation, db: Session = Depends(get_db)
):
    """
    Create a new group location association in the database.
    """
    return await adder(db, GroupLocation, group_location_data)

@router.post("/owner", summary="Create a new owner")
async def create_owner(owner_data: CreateOwner, db: Session = Depends(get_db)):
    """
    Create a new owner in the database.
    """
    return await adder(db, Owner, owner_data)

@router.post("/contact", summary="Create a new contact")
async def create_contact(contact_data: CreateContact, db: Session = Depends(get_db)):
    return await adder(db, Contact, contact_data)



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


@router.get("/group", summary="Get groups")
async def get_groups(db: Session = Depends(get_db)):
    """
    Retrieve all groups from the database.
    """
    sql = select(Group)
    result = await db.execute(sql)
    return result.all()


# ============= EOF =============================================
