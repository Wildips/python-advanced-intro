from fastapi import FastAPI, HTTPException, Form

from mservice.model.new_user import NewUserResponse, NewUser
from mservice.model.user import UserResponse
from mservice.utils import get_data, response_user

app = FastAPI()


@app.get("/api/users/{user_id}")
async def get_user(user_id: int, page: int = 1, users_per_page: int = 12):
    users, support_info = get_data()

    total_pages = (len(users) + users_per_page - 1) // users_per_page
    if page < 1 or page > total_pages:
        raise HTTPException(status_code=404, detail="Page not found")

    if user_id in users:
        return UserResponse(data=users[user_id], support=support_info)
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/api/users", response_model=NewUserResponse, status_code=201)
async def post_create_users(new_user: NewUser):
    return response_user(name=new_user.name, job=new_user.job)


@app.post("/api/user", response_model=NewUserResponse, status_code=201)
async def post_create_user(
        name: str = Form(...),
        job: str = Form(...),
):
    return response_user(name=name, job=job)
