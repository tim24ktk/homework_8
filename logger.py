import json
import os


def create_new(data):
    """"
    записывает новый контакт в файл
    в случае, если файла нет, создает его
    """

    lst = []

    if not os.path.exists('data_file.json'):
        lst.append(data)
        with open('data_file.json', 'w', encoding='utf-8') as new_file:
            new_file.write(json.dumps(lst, indent=2))
    else:
        with open('data_file.json', 'r', encoding='utf-8') as file:
            data_file = json.load(file)

        data_file.append(data)
        with open('data_file.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(data_file, indent=2))


def get_data():
    """
    открывет файл для чтения
    """
    try:
        with open('data_file.json', 'r', encoding='utf-8') as read_file:
            return json.load(read_file)
    except FileNotFoundError:
        return False


def overwrite_file(data):
    """
    перезапись файла после удаления и редактирования
    """
    with open('data_file.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=2))
