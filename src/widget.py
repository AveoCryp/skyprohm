from datetime import datetime

from src.masks import mask_account, mask_card


def mask_number(input_str: str) -> str:
    """
    Принимает на вход строку с информацией — тип карты/счета и номер карты/счета.
    Возвращает исходную строку с замаскированным номером карты/счета.
    """
    if not input_str or not isinstance(input_str, str):
        return input_str

    split_str = input_str.split()
    if not split_str:
        return input_str

    if split_str[0] in ["Visa", "MasterCard", "Maestro"]:
        return " ".join(
            [*filter(str.isalpha, split_str),
             mask_card("".join([i for i in split_str if i.isdigit()]))]
        )
    elif split_str[0] == "Счет":
        return "Счет " + mask_account(split_str[1])
    return input_str


def convert_date_format(input_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат DD.MM.YYYY
    """
    if not input_str or not isinstance(input_str, str):
        return input_str

    try:
        input_date = datetime.strptime(input_str, "%Y-%m-%dT%H:%M:%S.%f")
        return input_date.strftime("%d.%m.%Y")
    except ValueError:
        return input_str
