import uvicorn

from mservice.config import HOST, PORT
from mservice.service import app

uvicorn.run(app, host=HOST, port=PORT)
