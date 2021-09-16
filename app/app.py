from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Request,
)

from routes.userRoutes import router

import base64
import binascii

app = FastAPI()


app.include_router(router)