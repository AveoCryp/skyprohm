import pytest

from src.proccesing import filter_by_state, sort_by_date


def test_filter_by_state(test_data):
    # Тестирование фильтрации по EXECUTED
    result = filter_by_state(test_data, "EXECUTED")
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)

    # Тестирование фильтрации по PENDING
    result = filter_by_state(test_data, "PENDING")
    assert len(result) == 1
    assert all(item["state"] == "PENDING" for item in result)

    # Тестирование фильтрации по несуществующему статусу
    result = filter_by_state(test_data, "UNKNOWN")
    assert len(result) == 0


def test_sort_by_date(test_data):
    # Сортировка по убыванию (по умолчанию)
    result = sort_by_date(test_data)
    assert result[0]["id"] == 4
    assert result[-1]["id"] == 1

    # Сортировка по возрастанию
    result = sort_by_date(test_data, False)
    assert result[0]["id"] == 1
    assert result[-1]["id"] == 4

    # Тестирование с пустым списком
    assert sort_by_date([]) == []