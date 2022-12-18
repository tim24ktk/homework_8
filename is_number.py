# функция проверяет ли можно привести строку к вещественному числу,
# если нет то выбрасывает исключение
def is_number(value: str) -> bool:
    """
    функция проверяет ли можно привести строку к вещественному числу,
    если нет то выбрасывает исключение
    :param value: принимает на вход строку
    :return: True или False
    """
    try:
        float(value)
        return True
    except ValueError:
        return False
