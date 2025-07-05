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

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db import get_db_session
from db.series import TimeObservation, TimeSeries
from db.sample import Sample
from schemas.response.timeseries import WellTimeseriesResponse
from schemas.create.timeseries import (
    CreateTimeSeries,
    CreateSample,
    CreateTimeObservation,
)

router = APIRouter(
    prefix="/sample",
)


@router.post(
    "/timeseries/add",
    status_code=status.HTTP_201_CREATED,
)
def add_sample_timeseries(
    timeseries_data: CreateTimeSeries, session: Session = Depends(get_db_session)
):

    timeseries = TimeSeries(**timeseries_data.model_dump())
    session.add(timeseries)
    session.commit()
    return timeseries


@router.post("/add", status_code=status.HTTP_201_CREATED, summary="Add Sample")
def add_sample(
    sample_data: CreateSample,
    session: Session = Depends(get_db_session),
):
    """
    Endpoint to add a sample.
    """

    sample = Sample(**sample_data.model_dump())
    session.add(sample)
    session.commit()
    return sample


@router.post(
    "/timeseries/observations/add",
    status_code=status.HTTP_201_CREATED,
    summary="Add Sample Timeseries Observations",
)
def add_sample_observations(
    observations: List[CreateTimeObservation],
    session: Session = Depends(get_db_session),
):
    """
    Endpoint to add observations to a sample timeseries.
    """
    obs = []
    for observation in observations:
        data = observation.model_dump()
        ts = TimeObservation(**data)

        session.add(ts)
        obs.append(ts)

    session.commit()
    return obs


#
# @router.post(
#     "/well",
#     response_model=WellTimeseriesResponse,
#     summary="Add Well Timeseries",
#     status_code=status.HTTP_201_CREATED,
# )
# def add_well_timeseries(
#     well_timeseries_data: CreateWellTimeseries, session=Depends(get_db_session)
# ):
#     """
#     Endpoint to add a well timeseries.
#     """
#
#     ts = WellTimeseries(**well_timeseries_data.model_dump())
#     session.add(ts)
#     session.commit()
#
#     return ts
#
#
# @router.post(
#     "/well/groundwater_level/observations",
#     status_code=status.HTTP_201_CREATED,
#     summary="Add groundwater level observation",
# )
# def add_well_observations(
#     observations: List[CreateGroundwaterLevelObservation],
#     session=Depends(get_db_session),
# ):
#     """
#     Endpoint to add observations to a well timeseries.
#     """
#     for observation in observations:
#         ts = GroundwaterLevelObservation(**observation.model_dump())
#         session.add(ts)
#
#     session.commit()
#     return {"message": "Observations added successfully."}


# ============= EOF =============================================
