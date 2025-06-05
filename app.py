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

from models import sqlalchemy_sessionmaker, sqlalchemy_engine, Base
from admin.user import User


async def init_db():
    async with sqlalchemy_engine.begin() as c:
        await c.run_sync(Base.metadata.drop_all)
        await c.run_sync(Base.metadata.create_all)


async def create_superuser():
    async with sqlalchemy_sessionmaker() as s:
        user = User(
            username="admin",
            password="admin",
            is_superuser=True,
        )
        s.add(user)
        await s.commit()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await init_db()
    await create_superuser()
    yield


app = FastAPI(
    title="Sample Location API",
    description="API for managing sample locations",
    version="0.0.1",
    lifespan=lifespan,
)

from fastadmin import fastapi_app as admin_app

app.mount("/admin", admin_app)
# ============= EOF =============================================
