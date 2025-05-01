import pytest
from pytest_bdd import scenarios, given, when, then
from datetime import datetime

scenarios("../add_tasks.feature")


@pytest.fixture
def task_list():
    return []


@given("an empty task list")
def empty_list(task_list):
    task_list.clear()


@when('I add a task titled "Buy milk" with priority "High" and category "Personal"')
def add_buy_milk(task_list):
    task = {
        "id": len(task_list) + 1,
        "title": "Buy milk",
        "description": "",
        "priority": "High",
        "category": "Personal",
        "due_date": "2025-04-30",
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    task_list.append(task)


@when('I add a task titled "Read book" with priority "Low" and category "School"')
def add_read_book(task_list):
    task = {
        "id": len(task_list) + 1,
        "title": "Read book",
        "description": "",
        "priority": "Low",
        "category": "School",
        "due_date": "2025-05-10",
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    task_list.append(task)


@when("I attempt to add a task with no title")
def add_empty_title_task(task_list):
    task = {
        "id": len(task_list) + 1,
        "title": "",
        "description": "no title task",
        "priority": "Medium",
        "category": "Other",
        "due_date": "2025-04-30",
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    if task["title"]:
        task_list.append(task)


@then('the task list should contain 1 task with title "Buy milk"')
def assert_buy_milk_present(task_list):
    assert len(task_list) == 1
    assert task_list[0]["title"] == "Buy milk"


@then("the task list should contain 2 tasks")
def assert_two_tasks(task_list):
    assert len(task_list) == 2


@then("the task list should still be empty")
def assert_still_empty(task_list):
    assert len(task_list) == 0
