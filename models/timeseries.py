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
from sqlalchemy import DateTime, Float, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declared_attr
from sqlalchemy.testing.schema import mapped_column

from models import AutoBaseMixin, Base, PropertiesMixin


class TimeseriesMixin:
    @declared_attr
    def name(self):
        return mapped_column(String(100))

    @declared_attr
    def description(self):
        return mapped_column(String(255), nullable=True)


class WellTimeseries(Base, TimeseriesMixin, AutoBaseMixin, PropertiesMixin):
    well_id = mapped_column(
        "well_id", Integer, ForeignKey("well.id", ondelete="CASCADE"), nullable=False
    )

    equipment_id = mapped_column(
        "equipment_id", Integer, ForeignKey("equipment.id", ondelete="SET NULL"), nullable=True
    )


class GroundwaterLevelObservation(Base, AutoBaseMixin, PropertiesMixin):
    """
    Base class for time series observations.
    This class can be extended to create specific types of observations.
    """

    # Define common fields for observations here
    timestamp = mapped_column(DateTime, nullable=False)
    value = mapped_column(Float, nullable=False)
    description = mapped_column(String(255), nullable=True)

    def __repr__(self):
        return f"<Observation(id={self.id}, timestamp={self.timestamp}, value={self.value})>"


# ============= EOF =============================================
