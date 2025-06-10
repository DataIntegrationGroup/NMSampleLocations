import os

from fastapi_pagination import add_pagination

os.environ["ADMIN_USER_MODEL"] = "User"
os.environ["ADMIN_USER_MODEL_USERNAME_FIELD"] = "username"
os.environ["ADMIN_SECRET_KEY"] = "secret"

from starlette.middleware.cors import CORSMiddleware

from app import app

from fastadmin import fastapi_app as admin_app

from routes.base import router as base_router
# from routes.lut import router as lut_router
from routes.form import router as form_router
from routes.timeseries import router as timeseries_router
from routes.lexicon import router as lexicon_router

app.mount("/admin", admin_app)

app.include_router(base_router)
# app.include_router(lut_router)
app.include_router(form_router)
app.include_router(timeseries_router)
app.include_router(lexicon_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust as needed for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_pagination(app)

# import all the admin models
from admin.user import UserModelAdmin
from admin.base import SampleLocationsAdmin, WellAdmin


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
