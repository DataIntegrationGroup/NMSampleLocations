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

from models import get_db_session
from models.timeseries import WellTimeseries
from schemas.timeseries import CreateWellTimeseries, WellTimeseriesResponse

router = APIRouter(
    prefix="/timeseries",
)


@router.post(
    "/well", response_model=WellTimeseriesResponse, summary="Add Well Timeseries"
)
def add_well_timeseries(
    well_timeseries_data: CreateWellTimeseries, session=Depends(get_db_session)
):
    """
    Endpoint to add a well timeseries.
    """

    ts = WellTimeseries(**well_timeseries_data.model_dump())
    session.add(ts)
    session.commit()

    return ts


# ============= EOF =============================================
