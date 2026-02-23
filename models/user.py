from models.task import Task

class User:
    def __init__(self, username, password, tasks=None):
        self.username = username
        self.password = password
        self.tasks = tasks if tasks else []

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "tasks": [t.to_dict() for t in self.tasks],
        }

    @staticmethod
    def from_dict(data):
        tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return User(data["username"], data["password"], tasks)