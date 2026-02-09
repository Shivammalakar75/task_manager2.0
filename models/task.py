class Task:
    def __init__(self, task_id: int, title: str, description: str, status: str = "Pending"):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Task(
            data["id"],
            data["title"],
            data["description"],
            data["status"],
        )

    def __str__(self):
        return f"{self.id} | {self.title} | {self.description} | {self.status}"