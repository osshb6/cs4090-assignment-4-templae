from json import JSONDecodeError
import pytest
from src.tasks import load_tasks


def test_load_tasks_valid_json(mocker):
    mock_data = '[{"id": 1, "title": "a", "description": "aaa", "priority": "Low", "category": "Work", "due_date": "2025-04-10", "completed": true, "created_at": "2025-04-10 17:54:06"}]'
    mocked_open = mocker.mock_open(read_data=mock_data)
    mocker.patch("builtins.open", mocked_open)

    result = load_tasks("fake_path.json")
    assert result == [{'category': 'Work',
                          'completed': True,
                          'created_at': '2025-04-10 17:54:06',
                          'description': 'aaa',
                          'due_date': '2025-04-10',
                          'id': 1,
                          'priority': 'Low',
                          'title': 'a'}]
    mocked_open.assert_called_once_with("fake_path.json", "r")


def test_load_tasks_file_not_found(mocker):
    mocker.patch("builtins.open", side_effect=FileNotFoundError)

    result = load_tasks("nonexistent.json")
    assert result == []


def test_load_tasks_invalid_json(mocker, capfd):
    mocked_open = mocker.mock_open(read_data="{bad json}")
    mocker.patch("builtins.open", mocked_open)

    mocker.patch(
        "json.load",
        side_effect=JSONDecodeError("Expecting value", doc="", pos=0)
    )

    result = load_tasks("corrupt.json")
    assert result == []

    out, _ = capfd.readouterr()
    assert "invalid JSON" in out