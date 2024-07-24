from fastapi import FastAPI, HTTPException

from mservice.model.user import UserResponse
from mservice.utils import get_data

app = FastAPI()


@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    users, support_info = get_data()
    if user_id in users:
        return UserResponse(data=users[user_id], support=support_info)
    else:
        raise HTTPException(status_code=404, detail="User not found")
