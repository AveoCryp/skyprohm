import pytest
from datetime import datetime

@pytest.fixture
def test_data():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00.000000",
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            }
        },
        {
            "id": 2,
            "state": "PENDING",
            "date": "2023-01-02T12:00:00.000000",
            "description": "Перевод со счета на счет",
            "operationAmount": {
                "amount": "2000.00",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            }
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-01-03T12:00:00.000000",
            "description": "Перевод с карты на карту",
            "operationAmount": {
                "amount": "3000.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            }
        },
        {
            "id": 4,
            "state": "CANCELED",
            "date": "2023-01-04T12:00:00.000000",
            "description": "Отмена операции",
            "operationAmount": {
                "amount": "4000.00",
                "currency": {
                    "name": "GBP",
                    "code": "GBP"
                }
            }
        }
    ]

@pytest.fixture
def card_numbers():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("1234", "Некорректный номер карты")
    ]

@pytest.fixture
def account_numbers():
    return [
        ("12345678", "**5678"),
        ("987654321", "**4321"),
        ("123", "Некорректный номер счета")
    ]

@pytest.fixture
def mixed_inputs():
    return [
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
        ("Счет 12345678", "Счет **5678"),
        ("Неизвестный тип 12345678", "Неизвестный тип 12345678")
    ]

@pytest.fixture
def date_inputs():
    return [
        ("2023-01-01T12:00:00.000000", "01.01.2023"),
        ("2022-12-31T23:59:59.999999", "31.12.2022"),
        ("2020-02-29T00:00:00.000000", "29.02.2020")  # високосный год
    ]