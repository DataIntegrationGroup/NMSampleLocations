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
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from models import sqlalchemy_sessionmaker, engine, Base
from models.lexicon import Lexicon
from settings import settings


def init_db():
    """
    Initialize the database by creating all tables.
    This function is called during application startup.
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def init_lexicon():
    with open("lexicon.json") as f:
        import json

        default_lexicon = json.load(f)

    # populate lexicon
    with sqlalchemy_sessionmaker() as s:
        for term_dict in default_lexicon:
            s.add(Lexicon(**term_dict))
        s.commit()


def create_superuser():
    from admin.user import User

    with sqlalchemy_sessionmaker() as s:
        user = User(
            username="admin",
            password="admin",
            is_superuser=True,
        )
        s.add(user)
        s.commit()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Application lifespan event handler to initialize the database and lexicon.
    """
    if settings.get_enum("MODE") == "production":
        pass
    else:
        init_db()
        create_superuser()
        init_lexicon()
    yield


app = FastAPI(
    title="Sample Location API",
    description="API for managing sample locations",
    version="0.0.1",
    lifespan=lifespan,
)

# ============= EOF =============================================
