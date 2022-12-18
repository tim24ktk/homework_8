from datetime import datetime as dt


def select_action():
    print('''Выберите действие:
            1: запись контакта
            2: поиск контакта
            3: изменение контакта
            4: удаление контакта
            5: выход из справочника''')
    return int(input('-> '))


def add_contact(value=1):
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    e_mail = input('Введите e-mail: ')
    create_date = dt.now().strftime('%H:%M')

    return {'id': value, 'surname': surname, 'name': name, 'phone_number': phone_number, 'e_mail': e_mail,
            'create_date': create_date, 'update_date': ''}


def search_contact():
    return input('Введите данные контакта: ')


def show_contact(value):
    print('Результат поиска: ')

    for i in value:
        if isinstance(i, str):
            print(''.join(value))
            print()
        else:
            for k, v in i.items():
                print(f'{k}-> {v}')
            print()


def choose_element(indexes, data):
    print('Есть несколько контактов для удаления -> ')

    for i in indexes:
        print(f'Индекс {i} -> {data[i]}')

    return int(input('Введите индекс контакта который хотите удалить: '))


def update_value(data):
    print('Выберите данные которые хотите изменить -> ')
    surname = input('Измените фамилию: ')
    name = input('Измените имя: ')
    phone_number = input('Измените номер телефона: ')
    e_mail = input('Измените e-mail: ')
    update_date = dt.now().strftime('%H:%M')

    if surname == '':
        surname = data['surname']

    if name == '':
        name = data['name']

    if phone_number == '':
        phone_number = data['phone_number']

    if e_mail == '':
        e_mail = data['e_mail']

    return {'surname': surname, 'name': name, 'phone_number': phone_number, 'e_mail': e_mail, 'update_date': update_date}


def update_element(indexes, data):
    print('Есть несколько контактов для редактирования -> ')

    for i in indexes:
        print(f'Индекс {i} -> {data[i]}')

    return int(input('Введите индекс контакта который хотите радактировать: '))
