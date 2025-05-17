import pytest
from src.widget import mask_number, convert_date_format

@pytest.mark.parametrize("input_str, expected", [
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
    ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ("Счет 12345678", "Счет **5678"),
    ("Неизвестный тип 12345678", "Неизвестный тип 12345678"),
    ("", ""),
    (None, None)
])
def test_mask_number(input_str, expected):
    assert mask_number(input_str) == expected

@pytest.mark.parametrize("input_date, expected", [
    ("2023-01-01T12:00:00.000000", "01.01.2023"),
    ("2022-12-31T23:59:59.999999", "31.12.2022"),
    ("2020-02-29T00:00:00.000000", "29.02.2020"),
    ("", ""),
    (None, None)
])
def test_convert_date_format(input_date, expected):
    assert convert_date_format(input_date) == expected
