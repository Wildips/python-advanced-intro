import json

from mservice.config import HOST
from mservice.model.user import User, Support


def get_data():
    with open('mservice/data/users.json') as data_file:
        users = {}
        data = json.load(data_file)
        for row in data:
            users[row["id"]] = User(**row)
        support_data = Support(url=f"http://{HOST}/#support-heading",
                               text=f"Some text message from support")
        return users, support_data
