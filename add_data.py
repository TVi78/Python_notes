import return_data_file as rdf
import json
from datetime import datetime
from datetime import date


def add_note():
    print ("-------------------------------")
    note_title = input("Введите заголовок заметки: ")
    note_body = input("Введите тело заметки: ")
    save = input("Сохранить? д/н: ")
    if (save=="y" or save=="д"):
        list, id= rdf.data_file()
        id=int(id)+1
        with open('db/data.json', 'w', encoding='utf-8') as file:
            date=str(datetime.now())
            list.append({'id': id, 'title':note_title, 'body': note_body, 'date': date})
            json.dump(list,file, indent=2)
        print("Заметка успешно сохранена!")
    else:
        print("Заметка не сохранена!")


