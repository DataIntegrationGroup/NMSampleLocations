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
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UUID,
    Float,
    Boolean,
    Text,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship, declared_attr, Mapped, mapped_column

from models import Base


class AutoBaseMixin:
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def created_at(self):
        return Column(DateTime, nullable=False, server_default=func.now())

    @declared_attr
    def updated_at(self):
        return Column(
            DateTime,
            nullable=False,
            server_default=func.now(),
            server_onupdate=func.now(),
        )


class SampleLocation(Base, AutoBaseMixin):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    visible = Column(Boolean, default=True, nullable=False)

    point = Column(Geometry('POINT', srid=4326))
    owner_id = Column(Integer, ForeignKey("owner.id"), nullable=True)


class Asset(Base, AutoBaseMixin):
    fs_path = Column(String(255), nullable=False, unique=True)
    name = Column(String(100), nullable=False, unique=True)
    file_type = Column(String(50), nullable=False)


class AssetLocation(Base, AutoBaseMixin):
    asset_id = Column(Integer, ForeignKey("asset.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("samplelocation.id"), nullable=False)

    asset = relationship("Asset")
    location = relationship("SampleLocation")


class Owner(Base, AutoBaseMixin):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)

    contacts = relationship(
        "Contact", back_populates="owner", cascade="all, delete-orphan"
    )


class Contact(Base, AutoBaseMixin):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    owner_id = Column(Integer, ForeignKey("owner.id"), nullable=False)

    owner = relationship("Owner")


class Well(Base, AutoBaseMixin):
    location_id = Column(Integer, ForeignKey("samplelocation.id"), nullable=False)
    well_depth = Column(Float, nullable=True)
    hole_depth = Column(Float, nullable=True)
    well_type = Column(
        String(50), nullable=True
    )  # e.g., "Production", "Observation", etc.

    # Define a relationship to samplelocations if needed
    location = relationship("SampleLocation")


class WellScreen(Base, AutoBaseMixin):
    well_id = Column(Integer, ForeignKey("well.id"), nullable=False)
    screen_depth_top = Column(Float, nullable=False)
    screen_depth_bottom = Column(Float, nullable=False)
    screen_type = Column(String(50), nullable=True)  # e.g., "PVC", "Steel", etc.

    # Define a relationship to well if needed
    well = relationship("Well")


class Group(Base, AutoBaseMixin):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)

    # Define a relationship to samplelocations if needed
    # locations = relationship("SampleLocation")


class GroupLocation(Base, AutoBaseMixin):
    group_id = Column(Integer, ForeignKey("group.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("samplelocation.id"), nullable=False)


# class Spring(Base):
#     __tablename__ = 'Spring'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     location_id = Column(Integer, ForeignKey('samplelocation.id'), nullable=False)
#
#     # Define a relationship to samplelocation if needed
#     location = relationship("samplelocation")
#
#
# class Stream(Base):
#     __tablename__ = 'Stream'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     location_id = Column(Integer, ForeignKey('samplelocation.id'), nullable=False)
#
#     # Define a relationship to samplelocation if needed
#     location = relationship("samplelocation")
#
#
# class Surface(Base):
#     __tablename__ = 'Surface'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     location_id = Column(Integer, ForeignKey('samplelocation.id'), nullable=False)
#
#     # Define a relationship to samplelocation if needed
#     location = relationship("samplelocation")
#
#
# class Subsurface(Base):
#     __tablename__ = 'Subsurface'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     location_id = Column(Integer, ForeignKey('samplelocation.id'), nullable=False)
#
#     # Define a relationship to samplelocation if needed
#     location = relationship("samplelocation")
#


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(length=255), nullable=False)
    password: Mapped[str] = mapped_column(String(length=255), nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    avatar_url: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __str__(self):
        return self.username


# ============= EOF =============================================
