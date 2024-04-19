from datetime import datetime
import json
import return_data_file as rdf

def change_note():
    list, id=rdf.data_file()
    with open(f'db/data.json', 'r') as file:
        data=file.read()
        list=json.loads(data)
        id_list=[]
        for dict in list:
            id_list.append(dict["id"])
    id_edit = int(input(f"Введите один из следующих идентификаторов заметки "
                           f"{id_list}: "))
    if id_edit not in id_list:
        id_edit = int(input(f"Ошибка!"
                               f"Введите один из следующих идентификаторов "
                               f"{id_list}: "))
    new_title = input("Введите заголовок заметки: ")
    new_body = input("Введите тело заметки: ")
    save = input("Сохранить? д/н: ")
    if (save=="y" or save=="д"):
        with open('db/data.json', 'w') as file:
            new_date=str(datetime.now())
            for dict in list:
                if dict["id"]==id_edit:
                    dict["title"]=new_title
                    dict["body"]=new_body
                    dict["date"]=new_date
            json.dump(list,file, indent=2)
        print("Данные успешно изменены!")
