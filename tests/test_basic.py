import pytest
from src.tasks import generate_unique_id, filter_tasks_by_priority, search_tasks, filter_tasks_by_category, \
    filter_tasks_by_completion, get_overdue_tasks


def test_generate_unique_id_empty_list():
    tasks = []
    assert generate_unique_id(tasks) == 1

def test_generate_unique_id_nonempty_list():
    tasks = [
        {"id": 4},
        {"id": -1},
        {"id": 6},
    ]
    assert generate_unique_id(tasks) == 7

def test_filter_tasks_by_priority_matches():
    tasks = [
        {"id": 1, "name": "Task 1", "priority": "High"},
        {"id": 2, "name": "Task 2", "priority": "Low"},
        {"id": 3, "name": "Task 3", "priority": "Low"},
    ]
    expected = [
        {"id": 2, "name": "Task 2", "priority": "Low"},
        {"id": 3, "name": "Task 3", "priority": "Low"},
    ]
    assert filter_tasks_by_priority(tasks, "Low") == expected

def test_filter_tasks_by_priority_none_found():
    tasks = [
        {"id": 1, "name": "Task 1", "priority": "High"},
        {"id": 2, "name": "Task 2", "priority": "Low"},
    ]
    expected = []
    assert filter_tasks_by_priority(tasks, "Medium") == expected

def test_filter_tasks_by_priority_empty_tasks():
    tasks = []
    expected = []
    assert filter_tasks_by_priority(tasks, "High") == expected

def test_filter_tasks_by_category_matches():
    tasks = [
        {"id": 1, "name": "Task 1", "category": "Work"},
        {"id": 2, "name": "Task 2", "category": "Work"},
        {"id": 3, "name": "Task 3", "category": "School"},
    ]
    expected = [
        {"id": 1, "name": "Task 1", "category": "Work"},
        {"id": 2, "name": "Task 2", "category": "Work"},
    ]
    assert filter_tasks_by_category(tasks, "Work") == expected

def test_filter_tasks_by_category_none_found():
    tasks = [
        {"id": 1, "name": "Task 1", "category": "Work"},
        {"id": 2, "name": "Task 2", "category": "Work"},
        {"id": 3, "name": "Task 3", "category": "School"},
    ]
    expected = []
    assert filter_tasks_by_category(tasks, "Other") == expected

def test_filter_tasks_by_category_empty_tasks():
    tasks = []
    expected = []
    assert filter_tasks_by_category(tasks, "Other") == expected

def test_filter_tasks_by_completion_matches():
    tasks = [
        {"id": 1, "name": "Task 1", "completed": True},
        {"id": 2, "name": "Task 2", "priority": False},
    ]
    expected = [
        {"id": 1, "name": "Task 1", "completed": True},
    ]
    assert filter_tasks_by_completion(tasks, True) == expected

def test_filter_tasks_by_completion_none_found():
    tasks = [
        {"id": 1, "name": "Task 1", "completed": True},
        {"id": 2, "name": "Task 2", "completed": True},
    ]
    expected = []
    assert filter_tasks_by_completion(tasks, False) == expected

def test_filter_tasks_by_completion_empty_tasks():
    tasks = []
    expected = []
    assert filter_tasks_by_completion(tasks, True) == expected

def test_search_tasks_title_match():
    tasks = [
        {"id": 1, "title": "Wake up", "description": "I need to wake up from my dream"},
        {"id": 2, "title": "Go to bed", "description": "I need to go to sleep"},
    ]
    expected = [{"id": 2, "title": "Go to bed", "description": "I need to go to sleep"}]
    assert search_tasks(tasks, "bed") == expected

def test_search_tasks_description_match():
    tasks = [
        {"id": 1, "title": "Wake up", "description": "I need to wake up from my dream"},
        {"id": 2, "title": "Go to bed", "description": "I need to go to sleep"},
    ]
    expected = [{"id": 2, "title": "Go to bed", "description": "I need to go to sleep"}]
    assert search_tasks(tasks, "sleep") == expected

def test_search_tasks_case_insensitive():
    tasks = [
        {"id": 1, "title": "Wake up", "description": "I need to wake up from my dream"},
        {"id": 2, "title": "Go to bed", "description": "I need to go to sleep"},
    ]
    expected = [{"id": 2, "title": "Go to bed", "description": "I need to go to sleep"}]
    assert search_tasks(tasks, "bed") == expected
    assert search_tasks(tasks, "BED") == expected

def test_search_tasks_no_match():
    tasks = [
        {"id": 1, "title": "Wake up", "description": "I need to wake up from my dream"},
        {"id": 2, "title": "Go to bed", "description": "I need to go to sleep"},
    ]
    expected = []
    assert search_tasks(tasks, "eat") == expected

def test_search_tasks_empty_tasks_list():
    tasks = []
    expected = []
    assert search_tasks(tasks, "bed") == expected

def test_search_tasks_title_and_description_missing():
    tasks = [
        {"id": 1, "name": "I need to go to bed"},
    ]
    expected = []
    assert search_tasks(tasks, "bed") == expected

def test_get_overdue_tasks_empty_list():
    assert get_overdue_tasks([]) == []