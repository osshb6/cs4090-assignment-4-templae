import pytest

from src.tasks import filter_tasks_by_due_range, set_task_priority, set_task_category


def test_filter_tasks_by_due_range_some_found():
    tasks = [
        {"id": 1, "due_date": "2025-04-01"},
        {"id": 2, "due_date": "2025-04-15"},
        {"id": 3, "due_date": "2025-05-01"},
    ]
    expected = [
        {"id": 2, "due_date": "2025-04-15"},
    ]
    assert filter_tasks_by_due_range(tasks, "2025-04-10", "2025-04-20") == expected


def test_filter_tasks_by_due_range_none_found():
    tasks = [
        {"id": 1, "due_date": "2025-03-01"},
        {"id": 2, "due_date": "2025-03-15"},
    ]
    expected = []
    assert filter_tasks_by_due_range(tasks, "2025-04-01", "2025-04-30") == expected


def test_filter_tasks_by_due_range_empty_tasks():
    tasks = []
    expected = []
    assert filter_tasks_by_due_range(tasks, "2025-04-01", "2025-04-30") == expected


def test_set_task_priority_successful():
    tasks = [
        {"id": 1, "priority": "Low"},
        {"id": 2, "priority": "High"},
    ]
    expected = [
        {"id": 1, "priority": "Medium"},
        {"id": 2, "priority": "High"},
    ]
    assert set_task_priority(tasks, 1, "Medium") is True
    assert tasks == expected


def test_set_task_priority_invalid_id():
    tasks = [
        {"id": 1, "priority": "Low"},
    ]
    assert set_task_priority(tasks, 3, "High") is False
    assert tasks == [{"id": 1, "priority": "Low"}]

def test_set_task_category_successful():
    tasks = [
        {"id": 1, "category": "Work"},
        {"id": 2, "category": "Personal"},
    ]
    expected = [
        {"id": 1, "category": "School"},
        {"id": 2, "category": "Personal"},
    ]
    assert set_task_category(tasks, 1, "School") is True
    assert tasks == expected


def test_set_task_category_invalid_id():
    tasks = [
        {"id": 1, "category": "Work"},
    ]
    assert set_task_category(tasks, 2, "Other") is False
    assert tasks == [{"id": 1, "category": "Work"}]