import json
import return_data_file as rdf


def delete_note():
    list, id = rdf.data_file()
    with open(f'db/data.json', 'r') as file:
        data=file.read()
        list=json.loads(data)
        id_list=[]
        for dict in list:
            id_list.append(dict["id"])
    del_id = int(input("Введите один из следующих идентификаторов заметки, которую хотите удалить "
                       f"{id_list}: "))
    if del_id not in id_list:
        del_id = int(input(f"Ошибка!"
                               f"Введите один из следующих идентификаторов "
                               f"{id_list}: "))
    with open(f'db/data.json', 'w') as file:
        for i in range(len(list)):
            if list[i]["id"]==del_id:
                list.pop(i)
        json.dump(list,file, indent=2)
    print("Заметка успешно удалена!")




    # data, nf = data_file()
    # count_rows = len(data)
    # if count_rows == 0:
    #     print("Файл пусто!")
    # else:
    #     number_row = int(input(f"Введите номер строки "
    #                            f"от 1 до {count_rows}: "))
    #     while number_row < 1 or number_row > count_rows:
    #         number_row = int(input(f"Ошибка!"
    #                                f"Введите номер строки "
    #                                f"от 1 до {count_rows}: "))
    #     del data[number_row - 1]
    #     data = [f'{i + 1};{data[i].split(";")[1]};'
    #             f'{data[i].split(";")[2]};'
    #             f'{data[i].split(";")[3]};'
    #             f'{data[i].split(";")[4]}'
    #             for i in range(len(data))]
    #     with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
    #         file.writelines(data)
    #     print("Строка успешно удалена!")
