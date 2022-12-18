import view as vw
import logger as log
import model as ml
import is_number as is_n


def run():
    while True:
        select_action = vw.select_action()

        if is_n.is_number(select_action):
            data_file = log.get_data()

            if select_action == 1:

                if not data_file:
                    last_id = 1
                else:
                    last_id = int(ml.get_last_id(data_file)) + 1

                create_new = vw.add_contact(last_id)
                log.create_new(create_new)
                print('Контакт добавлен!')
                print()
            elif select_action == 2:
                view_search = vw.search_contact()
                result = ml.search_contact(data_file, view_search)
                vw.show_contact(result)
            elif select_action == 3:
                view_search = vw.search_contact()
                result = ml.search_contact(data_file, view_search)

                if isinstance(result[0], dict):
                    indexes = []

                    for value in result:
                        indexes.append(int(data_file.index(value)))

                    if len(indexes) == 1:
                        query = vw.update_value(data_file[0])
                        updated_file = ml.update_contact(query, data_file, indexes[0])
                        log.overwrite_file(updated_file)
                        print(f'Данные успешно изменены!')
                    else:
                        select_element = vw.update_element(indexes, data_file)
                        query = vw.update_value(data_file[select_element])
                        updated_file = ml.update_contact(query, data_file, select_element)
                        log.overwrite_file(updated_file)
                        print(f'Данные успешно изменены!')
                else:
                    print(''.join(result[0]))
            elif select_action == 4:
                view_search = vw.search_contact()
                result = ml.search_contact(data_file, view_search)

                if isinstance(result[0], dict):
                    indexes = []
                    for value in result:
                        indexes.append(int(data_file.index(value)))

                    if len(indexes) == 1:
                        new_data = ml.delete_contact(indexes[0], data_file)
                        log.overwrite_file(new_data)
                        print(f'Контакт удален!')
                    else:
                        choose_element = vw.choose_element(indexes, data_file)
                        new_data = ml.delete_contact(choose_element, data_file)
                        log.overwrite_file(new_data)
                        print(f'Контакт удален!')
                else:
                    print(''.join(result[0]))

            elif select_action == 5:
                exit()
        else:
            print('Вы ввели неверное значение! Попробуйте снова!')