import unittest
from unittest.mock import patch
from ToDoClass import Task, TaskList
import main


class TestTaskList(unittest.TestCase):
    def setUp(self):
        self.task_list = TaskList()

    def test_add_task(self):
        self.task_list.add_task("Buy milk")

        self.assertEqual(self.task_list.tasks, {1: "Buy milk"})

    def test_add_task_assigns_incrementing_ids(self):
        self.task_list.add_task("Buy milk")
        self.task_list.add_task("Walk dog")

        self.assertEqual(self.task_list.tasks, {1: "Buy milk", 2: "Walk dog"})

    def test_view_tasks_with_no_tasks(self):
        """ Since view_tasks only prints to console,
        we must use patch to capture the output, THEN we can assert 
        it with the self.assert test. It's like a simulation of the output"""
        #standard syntax below. the "builtins.print" means
        #the print function, which is built in to python. 
        #then we us 'as' to store the simulation in the mock_print variable
        with patch("builtins.print") as mock_print:
            self.task_list.view_tasks() #this is where the stdout is captured
        
        #now we take mock_print and assert that it was called 
        #only once and with the string we expect.
        mock_print.assert_called_once_with("No active tasks.\n")

    def test_view_tasks_with_tasks(self):
        """ See def task_view_tasks_with_no_tasks
        for an explanation of what's happening here. Only
        difference is we use add_task to actually add a task. 
        Then we need to verify view_task prints that list item as we expect. """
        self.task_list.add_task("Buy milk")

        with patch("builtins.print") as mock_print:
            self.task_list.view_tasks()

        mock_print.assert_any_call("1. Buy milk")

    def test_delete_task(self):
        self.task_list.add_task("Buy milk")

        self.task_list.delete_task(1)

        self.assertEqual(self.task_list.tasks, {})

    def test_delete_task_ignores_missing_id(self):
        self.task_list.add_task("Buy milk")

        self.task_list.delete_task(99)

        self.assertEqual(self.task_list.tasks, {1: "Buy milk"})


class TestMainMenu(unittest.TestCase):
    def setUp(self):
        # main.py tracks tasks in a module-level TaskList; reset it
        # between tests so cases don't leak state into each other.
        main.activeTaskList = TaskList()

    @patch("builtins.input", side_effect=["1", "Buy milk", "4"])
    def test_add_task_via_menu(self, mock_input):
        main.main()

        self.assertEqual(main.activeTaskList.tasks, {1: "Buy milk"})

    @patch("builtins.input", side_effect=["1", "", "4"])
    def test_add_task_via_menu_rejects_empty_name(self, mock_input):
        main.main()

        self.assertEqual(main.activeTaskList.tasks, {})

    @patch("builtins.input", side_effect=["3", "1", "4"])
    def test_delete_task_via_menu(self, mock_input):
        main.activeTaskList.add_task("Buy milk")

        main.main()

        self.assertEqual(main.activeTaskList.tasks, {})

    @patch("builtins.input", side_effect=["9", "4"])
    def test_invalid_choice_via_menu(self, mock_input):
        with patch("builtins.print") as mock_print:
            main.main()

        mock_print.assert_any_call("Invalid choice. Please try again.")


if __name__ == "__main__":
    unittest.main()
