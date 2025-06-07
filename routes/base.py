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
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import get_db
from models.base import (
    Well,
    SampleLocation,
    Group,
    GroupLocation,
    Owner,
    Contact,
    WellScreen,
    Spring, Equipment,
)
from schemas.base_get import GetWell,GetLocation, GetGroup
from schemas.base_create import (CreateWell, CreateLocation, CreateGroup, CreateGroupLocation, CreateOwner,
                                 CreateContact, CreateScreenWell, CreateSpring, CreateEquipment)

from schemas.base_responses import OwnerResponse, SampleLocationResponse, WellResponse, GroupResponse, ContactResponse, \
    WellScreenResponse, GroupLocationResponse, SpringResponse, EquipmentResponse

router = APIRouter(
    prefix="/base",
)


async def adder(session, table, model):
    """
    Helper function to add a new record to the database.
    """
    obj = table(**model.model_dump())
    session.add(obj)
    session.commit()
    return obj


@router.post(
    "/location", response_model=GetLocation, summary="Create a new sample location"
)
async def create_location(location_data: CreateLocation, session: Session = Depends(get_db)):
    """
    Create a new sample location in the database.
    """
    return await adder(session, SampleLocation, location_data)


@router.post("/well", response_model=GetWell, summary="Create a new well")
async def create_well(well_data: CreateWell, session: Session = Depends(get_db)):
    """
    Create a new well in the database.
    """
    return await adder(session, Well, well_data)


@router.post("/wellscreen", summary="Create a new well screen")
async def create_wellscreen(
    well_screen_data: CreateScreenWell, session: Session = Depends(get_db)
):
    """
    Create a new well screen in the database.
    """
    return await adder(session, WellScreen, well_screen_data)


@router.post("/group", summary="Create a new group")
async def create_group(group_data: CreateGroup, session: Session = Depends(get_db)):
    """
    Create a new group in the database.
    """
    return await adder(session, Group, group_data)


@router.post("/group_location", summary="Create a new group location")
async def create_group_location(
    group_location_data: CreateGroupLocation, session: Session = Depends(get_db)
):
    """
    Create a new group location association in the database.
    """
    return await adder(session, GroupLocation, group_location_data)


@router.post("/owner", summary="Create a new owner")
async def create_owner(owner_data: CreateOwner, session: Session = Depends(get_db)):
    """
    Create a new owner in the database.
    """
    return await adder(session, Owner, owner_data)


@router.post("/contact", summary="Create a new contact")
async def create_contact(contact_data: CreateContact, session: Session = Depends(get_db)):
    return await adder(session, Contact, contact_data)


@router.post("/spring", summary="Create a new spring")
async def create_spring(spring_data: CreateSpring, session: Session = Depends(get_db)):
    """
    Create a new spring in the database.
    """
    return await adder(session, Spring, spring_data)

@router.post("/equipment", summary="Create a new equipment")
async def create_equipment(equipment_data: CreateEquipment, session: Session = Depends(get_db)):
    """
    Create a new equipment in the database.
    """
    # Placeholder for actual equipment creation logic
    # return {"message": "This endpoint will create a new equipment."}
    return await adder(session, Equipment, equipment_data)

# ==== Get ============================================
@router.get(
    "/location",
    response_model=List[SampleLocationResponse],
    summary="Get all locations",
)
async def get_location(session: Session = Depends(get_db)):
    """
    Retrieve all wells from the database.
    """
    # Placeholder for actual database retrieval logic
    # return {"message": "This endpoint will return all wells."}
    # sql = select(SampleLocation)
    # result = db.execute(sql)
    # return result
    return simple_all_getter(session, SampleLocation)


@router.get("/well", response_model=List[WellResponse], summary="Get all wells")
async def get_wells(
    api_id: str = None, ose_pod_id: str = None, session: Session = Depends(get_db)
):
    """
    Retrieve all wells from the database.
    """

    if api_id:
        sql = select(Well).where(Well.api_id == api_id)
    elif ose_pod_id:
        sql = select(Well).where(Well.ose_pod_id == ose_pod_id)
    else:
        # If no parameters, return all wells
        return simple_all_getter(session, Well)

    result = session.execute(sql)
    return result.scalars().all()



@router.get("/group", response_model=List[GroupResponse], summary="Get groups")
async def get_groups(session: Session = Depends(get_db)):
    """
    Retrieve all groups from the database.
    """
    # sql = select(Group)
    # result = db.execute(sql)
    # return result.all()
    return simple_all_getter(session, Group)


@router.get("/owner", response_model=List[OwnerResponse], summary="Get owners")
async def get_owners(session: Session = Depends(get_db)):
    """
    Retrieve all owners from the database.
    """
    return simple_all_getter(session, Owner)
    # result = db.execute(sql)
    # return result.all()


@router.get("/contact", response_model=List[ContactResponse], summary="Get contacts")
async def get_contacts(session: Session = Depends(get_db)):
    """
    Retrieve all contacts from the database.
    :param session:
    :return:
    """
    return simple_all_getter(session, Contact)


@router.get(
    "/wellscreen", response_model=List[WellScreenResponse], summary="Get well screens"
)
async def get_well_screens(session: Session = Depends(get_db)):
    """
    Retrieve all well screens from the database.
    """
    return simple_all_getter(session, WellScreen)


@router.get(
    "/group_location",
    response_model=List[GroupLocationResponse],
    summary="Get group locations",
)
async def get_group_locations(session: Session = Depends(get_db)):
    """
    Retrieve all group locations from the database.
    """
    return simple_all_getter(session, GroupLocation)


@router.get(
    "/spring",
    response_model=List[SpringResponse],
)
async def get_springs(session: Session = Depends(get_db)):
    """
    Retrieve all springs from the database.
    """
    return simple_all_getter(session, Spring)


@router.get("/equipment", response_model=List[EquipmentResponse], summary="Get equipment")
async def get_equipment(session: Session = Depends(get_db)):
    """
    Retrieve all equipment from the database.
    """
    return simple_all_getter(session, Equipment)


# ============= Get by ID ============================================
@router.get("/equipment/{equipment_id}", response_model=EquipmentResponse, summary="Get equipment by ID")
async def get_equipment_by_id(equipment_id: int, session: Session = Depends(get_db)):
    """
    Retrieve an equipment by ID from the database.
    """
    equipment = simple_get_by_id(session, Equipment, equipment_id)
    if not equipment:
        return {"message": "Equipment not found"}
    return equipment


@router.get(
    "/spring/{spring_id}", response_model=SpringResponse, summary="Get spring by ID"
)
async def get_spring_by_id(spring_id: int, session: Session = Depends(get_db)):
    """
    Retrieve a spring by ID from the database.
    """
    spring = simple_get_by_id(session, Spring, spring_id)
    if not spring:
        return {"message": "Spring not found"}
    return spring


@router.get(
    "/owner/{owner_id}", response_model=OwnerResponse, summary="Get owner by ID"
)
async def get_owner_by_id(owner_id: int, session: Session = Depends(get_db)):
    """
    Retrieve an owner by ID from the database.
    """
    owner = simple_get_by_id(session, Owner, owner_id)
    if not owner:
        return {"message": "Owner not found"}
    return owner


@router.get(
    "/location/{location_id}",
    response_model=SampleLocationResponse,
    summary="Get location by ID",
)
async def get_location_by_id(location_id: int, session: Session = Depends(get_db)):
    """
    Retrieve a sample location by ID from the database.
    """
    location = simple_get_by_id(session, SampleLocation, location_id)
    if not location:
        return {"message": "Location not found"}
    return location


@router.get("/well/{well_id}", response_model=WellResponse, summary="Get well by ID")
async def get_well_by_id(well_id: int, session: Session = Depends(get_db)):
    """
    Retrieve a well by ID from the database.
    """
    well = simple_get_by_id(session, Well, well_id)
    if not well:
        return {"message": "Well not found"}
    return well


@router.get(
    "/wellscreen/{wellscreen_id}",
)
async def get_well_screen_by_id(wellscreen_id: int, session: Session = Depends(get_db)):
    """
    Retrieve a well screen by ID from the database.
    """
    well_screen = simple_get_by_id(session, WellScreen, wellscreen_id)
    if not well_screen:
        return {"message": "Well screen not found"}
    return well_screen


@router.get(
    "/group/{group_id}", response_model=GroupResponse, summary="Get group by ID"
)
async def get_group_by_id(group_id: int, session: Session = Depends(get_db)):
    """
    Retrieve a group by ID from the database.
    """
    group = simple_get_by_id(session, Group, group_id)
    if not group:
        return {"message": "Group not found"}
    return group


@router.get(
    "/group_location/{group_location_id}",
    response_model=GroupLocationResponse,
    summary="Get group location by ID",
)
async def get_group_location_by_id(
    group_location_id: int, session: Session = Depends(get_db)
):
    """
    Retrieve a group location by ID from the database.
    """
    group_location = simple_get_by_id(session, GroupLocation, group_location_id)
    if not group_location:
        return {"message": "Group location not found"}
    return group_location


@router.get(
    "/contact/{contact_id}", response_model=ContactResponse, summary="Get contact by ID"
)
async def get_contact_by_id(contact_id: int, session: Session = Depends(get_db)):
    """
    Retrieve a contact by ID from the database.
    """
    contact = simple_get_by_id(session, Contact, contact_id)
    if not contact:
        return {"message": "Contact not found"}
    return contact


def simple_get_by_id(session, table, item_id):
    """
    Helper function to get a record by ID from the database.
    """
    sql = select(table).where(table.id == item_id)
    result = session.execute(sql)
    return result.scalar_one_or_none()


def simple_all_getter(session, table):
    """
    Helper function to get records from the database.
    """
    sql = select(table)
    result = session.execute(sql)
    return result.scalars().all()


# ============= EOF =============================================
