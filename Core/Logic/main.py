import base64
import binascii

from fastapi import FastAPI, HTTPException, Request, status
from routes.user_routes import user_router

from views.dependencies import authenticate_user

app = FastAPI()

@app.middleware("http")
async def authenticate(request:Request, call_next):
    if "Authorization" in request.headers:
        auth = request.headers["Authorization"]
        try:
            scheme, creds = auth.split()
            if scheme.lower() == 'basic':
                decoded = base64.b64decode(creds).decode("ascii")
                username, _, password = decoded.partition(":")
                request.state.user = await authenticate_user(username, password)
        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid basic authentication"
            )
            
    response = await call_next(request)
    return response


app.include_router(user_router)
