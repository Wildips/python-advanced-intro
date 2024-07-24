import uvicorn

from mservice.config import HOST
from mservice.service import app

uvicorn.run(app, host=HOST, port=8000)
