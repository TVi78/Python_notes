import add_data as add_row
import delete_data as delete_row
import change_data as change_row
import copy_data as copy_row
import print_data as print_file


def check_note(n):
    while n < 1 or n > 6:
        print ("-------------------------------")
        n = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 6\n"
                      "Выберите функцию:\n"
                      "1. Добавить заметку\n"
                      "2. Удалить заметку\n"
                      "3. Редактировать заметку\n"
                      "4. Копировать заметку\n"
                      "5. Прочитать заметки\n"
                      "6. Выход\n"
                      "Введите номер команды: "))
        print ("-------------------------------")
    return n


def start_menu():
    command = None
    while command != 6:
        print ("-------------------------------")
        command = int(input("Доброго времени суток!\n"
                            "Выберите функцию:\n"
                            "1. Добавить заметку\n"
                            "2. Удалить заметку\n"
                            "3. Редактировать заметку\n"
                            "4. Копировать заметку\n"
                            "5. Прочитать заметки\n"
                            "6. Выход\n"
                            "Введите номер команды: "))
        command = check_note(command)
        if command == 1:
            add_row.add_note()
        elif command == 2:
            delete_row.delete_note()
        elif command == 3:
            change_row.change_note()
        elif command == 4:
            copy_row.copy_note()
        elif command == 5:
            print_file.print_file()
    print("Всего доброго!")