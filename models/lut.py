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
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from models import Base


class LUT_Well_Type(Base):
    """
    Represents a well type in the LU (Land Use) database.
    """

    __tablename__ = "lut_well_type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def __repr__(self):
        return f"<LUT_Well_Type(name={self.name}, description={self.description})>"


class LU_Formation_Zone(Base):
    """
    Represents a formation zone in the LU (Land Use) database.
    """

    __tablename__ = "lut_formation_zone"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def __repr__(self):
        return f"<LUT_Formation_Zone(name={self.name}, description={self.description})>"


# ============= EOF =============================================
