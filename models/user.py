from models.task import Task


class User:
    def __init__(self, username, password, tasks=None):
        self.username = username
        self.password = password
        self.tasks = tasks if tasks else []


    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        self.tasks.append(Task(task_id, title, description))

    def get_tasks(self, status=None):
        if status:
            return [t for t in self.tasks if t.status == status]
        return self.tasks

    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def print_tasks(self, tasks=None):
        tasks = tasks if tasks is not None else self.tasks

        if not tasks:
            print("No tasks found.")
            return

        print("=" * 70)
        print("ID | Title | Description | Status")
        print("-" * 70)

        for t in tasks:
            print(t)

        print("=" * 70)

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "tasks": [t.to_dict() for t in self.tasks],
        }

    @staticmethod
    def from_dict(data):
        tasks = [Task.from_dict(t) for t in data.get("tasks", [])]

        return User(
            data["username"],
            data["password"],
            tasks
        )