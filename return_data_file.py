# Файл txt
# def data_file():
#     try:
#         with open('db/data.txt', 'r+', encoding='utf-8') as file:
#             data = file.readlines()
#     except IOError:
#         with open('db/data.txt', 'x', encoding='utf-8') as file:
#             data=""
#     return data

# Файл json
import json

def data_file():
    try:
        with open('db/data.json', 'r+', encoding='utf-8') as file:
            data=file.read()
            list=json.loads(data)
            if len(list)!=0:
                id=list[len(list)-1]['id']
            else:
                id=0
    except IOError:
        with open('db/data.json', 'x', encoding='utf-8') as file:
            list=[]
            id=0
    return list, id