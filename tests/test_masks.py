import pytest
from src.masks import mask_card, mask_account

@pytest.mark.parametrize("input_card, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("1234", "Некорректный номер карты"),
    ("", "Некорректный номер карты"),
    (None, "Некорректный номер карты")
])
def test_mask_card(input_card, expected):
    assert mask_card(input_card) == expected

@pytest.mark.parametrize("input_account, expected", [
    ("12345678", "**5678"),
    ("987654321", "**4321"),
    ("123", "Некорректный номер счета"),
    ("", "Некорректный номер счета"),
    (None, "Некорректный номер счета")
])
def test_mask_account(input_account, expected):
    assert mask_account(input_account) == expected
