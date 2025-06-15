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
from sqlalchemy import Integer, ForeignKey, Float, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import mapped_column

from models import AutoBaseMixin, Base


class WaterChemistryAnalysis(Base, AutoBaseMixin):
    """
    Represents a chemical analysis of a well.
    """

    __tablename__ = "water_chemistry_analysis"

    # Define your columns here, e.g.:
    # id = Column(Integer, primary_key=True)
    analysis_set_id = mapped_column(
        Integer, ForeignKey("water_chemistry_analysis_set.id")
    )
    value = mapped_column(Float)
    unit = mapped_column(String(100), ForeignKey("lexicon.term"), nullable=True)
    qualifier = mapped_column(String(100), nullable=True)
    analyte = mapped_column(String(100), ForeignKey("lexicon.term"), nullable=False)

    # result = Column(Float)
    # timestamp = Column(DateTime)

    # Add relationships if necessary
    # well = relationship("Well", backref="analyses")


class WaterChemistryAnalysisSet(Base, AutoBaseMixin):
    """
    Represents a set of chemical analyses for a well.
    This can be used to group multiple analyses together.
    """

    __tablename__ = "water_chemistry_analysis_set"

    well_id = mapped_column(Integer, ForeignKey("well.id"))
    description = mapped_column(String(255), nullable=True)

    collection_date = mapped_column(
        DateTime, nullable=True
    )  # Use appropriate type for date
    analysis_date = mapped_column(
        DateTime, nullable=True
    )  # Use appropriate type for date

    laboratory = mapped_column(
        String(255), nullable=True
    )  # Name of the laboratory that performed the analysis

    # Define relationships
    analyses = relationship("WaterChemistryAnalysis", backref="analysis_set")
    well = relationship("Well", backref="analysis_sets")


# ============= EOF =============================================
