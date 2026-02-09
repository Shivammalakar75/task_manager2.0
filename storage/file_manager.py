import json
import os
from models.user import User

USER_DATA_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USER_DATA_FILE):
        return {}

    with open(USER_DATA_FILE, "r") as f:
        try:
            raw = json.load(f)
        except json.JSONDecodeError:
            return {}

    users = {}
    for username, data in raw.items():
        users[username] = User.from_dict(data)

    return users


def save_users(users):
    os.makedirs("data", exist_ok=True)

    data = {uid: user.to_dict() for uid, user in users.items()}

    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)




