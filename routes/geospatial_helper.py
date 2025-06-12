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
import shapefile
from geoalchemy2.shape import to_shape
from shapely.wkt import loads as wkt_loads

def create_shapefile(locations, filename="locations.shp"):
    # Create a point shapefile
    with shapefile.Writer(filename, shapeType=shapefile.POINT) as shp:
        shp.field("name", "C")
        for loc in locations:
            # Assume loc.point is WKT or a Shapely geometry
            if isinstance(loc.point, str):
                geom = wkt_loads(loc.point)
            else:
                geom = to_shape(loc.point)
            shp.point(geom.x, geom.y)
            shp.record(loc.name)
# ============= EOF =============================================
