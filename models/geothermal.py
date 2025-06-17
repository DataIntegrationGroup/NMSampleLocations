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
from sqlalchemy import Integer, ForeignKey, Float, String
from sqlalchemy.testing.schema import mapped_column

from models import AutoBaseMixin, Base


class GeothermalTemperatureProfile(Base, AutoBaseMixin):
    """ """

    __tablename__ = "geothermal_temperature_profile"
    well_id = mapped_column(Integer, ForeignKey("well.id"))

    def __repr__(self):
        return f"<GeothermalTemperatureProfile(well_id={self.well_id})>"


class GeothermalBottomHoleTemperature(Base, AutoBaseMixin):
    """ """

    __tablename__ = "geothermal_bottom_hole_temperature"
    well_id = mapped_column(Integer, ForeignKey("well.id"))

    # depth = mapped_column(
    #     Float
    # )
    # depth_unit = mapped_column(String(100), ForeignKey("lexicon.term"), default='ft')

    temperature = mapped_column(
        Float
    )  # Assuming temperature is stored as a float (e.g., in degrees Celsius)
    temperature_unit = mapped_column(
        String(100), ForeignKey("lexicon.term"), default="F"
    )

    def __repr__(self):
        return f"<GeothermalBottomHoleTemperature(well_id={self.well_id}, temperature={self.temperature})>"


class GeothermalTemperatureProfileObservation(Base, AutoBaseMixin):
    """ """

    __tablename__ = "geothermal_temperature_profile_observation"

    temperature_profile_id = mapped_column(
        Integer, ForeignKey("geothermal_temperature_profile.id")
    )
    depth = mapped_column(Float)
    depth_unit = mapped_column(String(100), ForeignKey("lexicon.term"), default="ft")

    temperature = mapped_column(
        Float
    )  # Assuming temperature is stored as a float (e.g., in degrees Celsius)
    temperature_unit = mapped_column(
        String(100), ForeignKey("lexicon.term"), default="F"
    )

    def __repr__(self):
        return (
            f"<GeothermalTemperatureProfileObservation(temperature_profile_id={self.temperature_profile_id}, "
            f"depth={self.depth}, temperature={self.temperature})>"
        )


class GeothermalWellInterval(Base, AutoBaseMixin):
    """ """

    __tablename__ = "geothermal_well_interval"

    well_id = mapped_column(Integer, ForeignKey("well.id"))
    top_depth = mapped_column(Float)
    bottom_depth = mapped_column(Float)
    depth_unit = mapped_column(String(100), ForeignKey("lexicon.term"), default="ft")

    def __repr__(self):
        return (
            f"<GeothermalWellInterval(well_id={self.well_id}, "
            f"top_depth={self.top_depth}, bottom_depth={self.bottom_depth})>"
        )


class GeothermalThermalConductivity(Base, AutoBaseMixin):
    """ """

    __tablename__ = "geothermal_thermal_conductivity"

    interval_id = mapped_column(Integer, ForeignKey("geothermal_well_interval.id"))
    conductivity = mapped_column(Float)  # Assuming conductivity is stored as a float
    conductivity_unit = mapped_column(
        String(100), ForeignKey("lexicon.term"), default="W/m·K"
    )

    def __repr__(self):
        return (
            f"<GeothermalThermalConductivity(interval_id={self.interval_id}, "
            f"thermal_conductivity={self.conductivity})>"
        )


class GeothermalHeatFlow(Base, AutoBaseMixin):
    """ """

    __tablename__ = "geothermal_heat_flow"

    interval_id = mapped_column(Integer, ForeignKey("geothermal_well_interval.id"))
    gradient = mapped_column(Float)  # Assuming gradient is stored as a float
    gradient_unit = mapped_column(
        String(100), ForeignKey("lexicon.term"), default="mW/m²"
    )

    ka = mapped_column(
        Float
    )  # Assuming ka is stored as a float (thermal diffusivity)
    ka_unit = mapped_column(
        String(100), ForeignKey("lexicon.term"), default="m²/s"
    )
    kpr = mapped_column(
        Float
    )  # Assuming kpr is stored as a float (thermal conductivity)
    kpr_unit = mapped_column(
        String(100), ForeignKey("lexicon.term"), default="W/m·K"
    )
    q = mapped_column(
        Float
    )  # Assuming q is stored as a float (heat flow)
    q_unit = mapped_column(
        String(100), ForeignKey("lexicon.term"), default="mW/m²"
    )

    pm = mapped_column(
        Float
    )  # Assuming pm is stored as a float (thermal power)
    pm_unit = mapped_column(
        String(100), ForeignKey("lexicon.term"), default="W/m²"
    )
# ============= EOF =============================================
