import pytest
import json
from src.utils.loader import load_data_from_json


def test_file_not_found():
    """Проверяет обработку отсутствующего файла"""
    with pytest.raises(FileNotFoundError):
        load_data_from_json("nonexistent_file.json")


def test_invalid_json(tmp_path):
    """Проверяет обработку невалидного JSON"""
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json}")

    with pytest.raises(json.JSONDecodeError):
        load_data_from_json(str(file_path))


def test_missing_fields(tmp_path):
    """Проверяет обработку отсутствующих обязательных полей """
    file_path = tmp_path / "missing_fields.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({"categories": [{"name": "Test"}]}, f)  # Нет description и products

    categories = load_data_from_json(str(file_path))
    assert len(categories) == 0  # Должен вернуть пустой список
