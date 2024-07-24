import json
from datetime import datetime, UTC
import random

from mservice.config import HOST
from mservice.model.user import User, Support


def get_data():
    with open('mservice/data/users.json') as data_file:
        users = {}
        data = json.load(data_file)
        for row in data:
            users[row["id"]] = User(id=row["id"], email=row["email"], first_name=row["first_name"],
                                    last_name=row["last_name"], avatar=row["avatar"])
        support_data = Support(url=f"http://{HOST}/#support-heading",
                               text=f"Some text message from support")
        return users, support_data


def response_user(name: str, job: str):
    return {
        "name": name,
        "job": job,
        "id": str(random.randint(100, 999)),
        "createdAt": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    }
