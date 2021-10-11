from fastapi.security import OAuth2PasswordBearer, oauth2
from passlib.context import CryptContext

import os
import motor.motor_asyncio as asyncio
import dotenv
# ================= Creating necessary variables ========================
#------------------ Token, authentication variables ---------------------
dotenv.dotenv_values(".env")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#----------------- Database variables (MongoDB) --------------------------
client = asyncio.AsyncIOMotorClient(os.environ["DB_URL"])
db = client.sahaayDB