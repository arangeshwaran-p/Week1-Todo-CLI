"""Basic unit tests for TaskManager."""

import unittest
from todo_cli.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Study Python")
        self.assertEqual(task["title"], "Study Python")
        self.assertFalse(task["completed"])

    def test_reject_empty_task(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        task = self.manager.add_task("Read a book")
        self.manager.complete_task(task["id"])
        self.assertTrue(task["completed"])

    def test_remove_task(self):
        task = self.manager.add_task("Exercise")
        self.manager.remove_task(task["id"])
        self.assertEqual(self.manager.get_tasks(), [])

    def test_unknown_task_id(self):
        with self.assertRaises(ValueError):
            self.manager.complete_task(99)

if __name__ == "__main__":
    unittest.main()
