"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

list_of_dicts = [
        {'name': "Петя", 
        'age': 18, 
        'job': "повар"
        },
        {'name': "Вова", 
        'age': 21, 
        'job': "хакер"
        },
        {'name': "Маша", 
        'age': 15, 
        'job': "дантист"
        },
        {'name': "Катя", 
        'age': 28, 
        'job': "модельер"
        }
    ]

def main():

    with open('list_of_dicts.csv', 'w', encoding='cp1251', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in list_of_dicts:
            writer.writerow(user)

if __name__ == "__main__":
    main()
