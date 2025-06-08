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
from fastapi.responses import JSONResponse

from models import get_db
from models.base import SampleLocation, Owner, Contact
from schemas.form import WellForm

router = APIRouter(prefix='/form')

@router.post("/well")
async def well_form(form_data: WellForm, session=Depends(get_db)):
    """
    Endpoint to handle well form submissions.
    """
    # add location to the database
    data = form_data.model_dump()
    location_data = data.get("location", None)
    owner_data = data.get("owner", None)

    location = SampleLocation(**location_data)
    session.add(location)
    # session.commit()

    contact_data = owner_data.pop("contact", None)

    owner = Owner(**owner_data)
    session.add(owner)
    # session.commit()

    for contact_info in contact_data:
        contact = Contact(**contact_info)
        contact.owner = owner
        session.add(contact)

    session.commit()

    return JSONResponse(status_code=201, content={"message": "Well form submitted successfully."})

# ============= EOF =============================================
