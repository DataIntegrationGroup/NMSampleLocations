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
import os

from geoalchemy2 import load_spatialite
from sqlalchemy import create_engine
from sqlalchemy.event import listen
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

if os.environ.get("SPATIALITE_LIBRARY_PATH") is None:
    os.environ["SPATIALITE_LIBRARY_PATH"] = "/opt/homebrew/lib/mod_spatialite.dylib"

# engine = create_async_engine(
#     "sqlite+aiosqlite:///./development.db",
#     echo=True,
#     plugins=['geoalchemy2'],
# )

engine = create_engine(
    "sqlite:///./development.db",
    echo=True,
    plugins=["geoalchemy2"],
)

listen(engine, "connect", load_spatialite)

# sqlalchemy_sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
sqlalchemy_sessionmaker = sessionmaker(engine, expire_on_commit=False)


async def get_db():
    session = sqlalchemy_sessionmaker()
    yield session
    session.close()


Base = declarative_base()



def adder(session, table, model):
    """
    Helper function to add a new record to the database.
    """
    obj = table(**model.model_dump())
    session.add(obj)
    session.commit()
    return obj
# ============= EOF =============================================
