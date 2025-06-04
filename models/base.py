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
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String, ForeignKey, UUID, Float
from sqlalchemy.orm import relationship

from models import Base


class SampleLocations(Base):
    __tablename__ = 'SampleLocations'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    # point = Column(Geometry(geometry_type='POINT', srid=4326))


class Wells(Base):
    __tablename__ = 'Wells'

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey('SampleLocations.id'), nullable=False)
    well_depth = Column(Float, nullable=False)
    hole_depth = Column(Float, nullable=False)
    # Define a relationship to SampleLocations if needed
    location = relationship("SampleLocations")


class Springs(Base):
    __tablename__ = 'Springs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey('SampleLocations.id'), nullable=False)

    # Define a relationship to SampleLocations if needed
    location = relationship("SampleLocations")


class Streams(Base):
    __tablename__ = 'Streams'

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey('SampleLocations.id'), nullable=False)

    # Define a relationship to SampleLocations if needed
    location = relationship("SampleLocations")


class Surfaces(Base):
    __tablename__ = 'Surfaces'

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey('SampleLocations.id'), nullable=False)

    # Define a relationship to SampleLocations if needed
    location = relationship("SampleLocations")


class Subsurfaces(Base):
    __tablename__ = 'Subsurfaces'

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey('SampleLocations.id'), nullable=False)

    # Define a relationship to SampleLocations if needed
    location = relationship("SampleLocations")




# ============= EOF =============================================
