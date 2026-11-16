"""Functions for managing to-do tasks."""

class TaskManager:
    def __init__(self):
        # A list keeps the first version simple and easy to understand.
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        title = title.strip()
        if not title:
            raise ValueError("Task description cannot be empty.")

        task = {
            "id": self.next_id,
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def remove_task(self, task_id):
        task = self.find_task(task_id)
        self.tasks.remove(task)
        return task

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        task["completed"] = True
        return task

    def find_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        raise ValueError(f"No task found with ID {task_id}.")

    def get_tasks(self):
        return self.tasks
