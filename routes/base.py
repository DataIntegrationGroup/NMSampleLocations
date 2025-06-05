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
from fastapi import APIRouter

router = APIRouter(
    prefix="/base",
)


@router.get("/wells", summary="Get all wells")
def get_wells():
    """
    Retrieve all wells from the database.
    """
    # Placeholder for actual database retrieval logic
    return {"message": "This endpoint will return all wells."}


# ============= EOF =============================================
