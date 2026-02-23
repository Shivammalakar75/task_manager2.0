from models.task import Task


class TaskService:

    @staticmethod
    def add_task(user, title, description):
        task_id = len(user.tasks) + 1
        task = Task(task_id, title, description)
        user.tasks.append(task)

    @staticmethod
    def get_tasks(user, status=None):
        if status:
            return [t for t in user.tasks if t.status == status]
        return user.tasks

    @staticmethod
    def find_task(user, task_id):
        for task in user.tasks:
            if task.id == task_id:
                return task
        return None

    @staticmethod
    def delete_task(user, task_id):
        user.tasks = [t for t in user.tasks if t.id != task_id]

    @staticmethod
    def update_task(user, task_id, new_description):
        task = TaskService.find_task(user, task_id)
        if task:
            task.description = new_description
            return True
        return False

    @staticmethod
    def mark_completed(user, task_id):
        task = TaskService.find_task(user, task_id)
        if task:
            task.mark_completed()
            return True
        return False

    @staticmethod
    def print_tasks(tasks):
        if not tasks:
            print("No tasks found.")
            return

        print(f"{'ID':<5}    {'Title':<25}    {'Description':<40}    {'Status':<12}")
        print("-" * 105)

        for t in tasks:
            title = (t.title[:22] + "...") if len(t.title) > 25 else t.title
            desc = (t.description[:37] + "...") if len(t.description) > 40 else t.description

            print(f"{t.id:<5}    {title:<25}    {desc:<40}    {t.status:<12}")