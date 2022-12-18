def get_last_id(data):
    """"
    возвращает id последней записи
    """
    return data[-1]['id']


def search_contact(data, contact):
    flag = True
    results = []

    for i in data:
        if contact in i.values():
            flag = False
            results.append(i)

    if flag:
        results.append(f'Контакт "{contact}" не найден')

    return results


def delete_contact(index, data):
    data.pop(index)
    return data


def update_contact(query, data_file, index):
    data_file[index].update(query)
    return data_file
