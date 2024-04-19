from datetime import datetime
import json


def print_file():
    with open('db/data.json', 'r+') as file:
                data=file.read()
                list=json.loads(data)
                new_date=[]
                for note in list:
                    date=note["date"]
                    date_new=datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
                    new_date.append(date_new)
                new_date=sorted(new_date) 
                for date_sr in new_date:
                    for i in list:
                        if (datetime.strptime(i["date"], "%Y-%m-%d %H:%M:%S.%f")==date_sr):
                              print(i) 
                    


        # datetime.datetime.strptime(<твоя переменная с dateTime из json>, "%Y-%m-%d %H:%M:%S.%f")

    # for i in range(1, 3):
    #     with open(f'db/data_{i}.txt', 'r', encoding='utf-8') as file:
    #         data = file.readlines()
    #     print(f"Вывод данных из {i}-ого файла:\n"
    #           f"{''.join(data)}")
    #     print()
