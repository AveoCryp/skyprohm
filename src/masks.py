def mask_card(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    if not card_number or not isinstance(card_number, str):
        return "Некорректный номер карты"
    if len(card_number) == 16:
        return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return "Некорректный номер карты"

def mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    if not account_number or not isinstance(account_number, str):
        return "Некорректный номер счета"
    if len(account_number) > 4:
        return "**" + account_number[-4:]
    return "Некорректный номер счета"
