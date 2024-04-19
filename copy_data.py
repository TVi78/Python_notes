from copy import deepcopy
from datetime import datetime
import json
import return_data_file as rdf

def copy_note():
    list, id = rdf.data_file()
    with open(f'db/data.json', 'r') as file:
        data=file.read()
        list=json.loads(data)
        id_list=[]
        for dict in list:
            id_list.append(dict["id"])
    copy_id = int(input("Введите один из следующих идентификаторов заметки, которую хотите скопировать " 
                        f"{id_list}: "))
    if copy_id not in id_list:
        copy_id = int(input(f"Ошибка!"
                               f"Введите один из следующих идентификаторов "
                               f"{id_list}: "))
    # note_copy={}
    with open(f'db/data.json', 'w') as file:
        new_date=str(datetime.now())
        note_copy=deepcopy(list)
        for dict in note_copy:
            if dict["id"]==copy_id:
                element=dict
                element["id"]=id+1
                element["date"]=new_date
        list.append(element)
        json.dump(list,file, indent=2)
    print("Заметка успешно скопирована и записана!")
