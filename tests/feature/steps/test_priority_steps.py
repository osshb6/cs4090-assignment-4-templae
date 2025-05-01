import pytest
from pytest_bdd import scenarios, given, when, then
from src.tasks import filter_tasks_by_priority, set_task_priority

scenarios("../priority.feature")

@pytest.fixture
def task_list():
    return []

@given("tasks with priorities High, Low, Low")
def task_priorities(task_list):
    task_list.extend([
        {"priority": "High"},
        {"priority": "Low"},
        {"priority": "Low"},
    ])

@given('a task with priority "Low"')
def task_with_low_priority(task_list):
    task_list.append({"id": 1, "priority": "Low"})

@when('I filter tasks by priority "Low"')
def filter_low_priority(task_list):
    task_list[:] = filter_tasks_by_priority(task_list, "Low")

@when('I change the task priority to "High"')
def change_priority(task_list):
    set_task_priority(task_list, 1, "High")

@then("I should get 2 tasks")
def assert_two_tasks(task_list):
    assert len(task_list) == 2

@then('the task should have priority "High"')
def assert_high(task_list):
    assert task_list[0]["priority"] == "High"
