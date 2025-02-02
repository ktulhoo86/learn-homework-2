"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

list_of_dicts = [{'name': 'Маша', 'age': 25, 'job': 'Scientist'},
                {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
                {'name': 'Дуся', 'age': 18, 'job': 'Small boss'},
                {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('some.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for dikt in list_of_dicts:
            writer.writerow(dikt)


if __name__ == "__main__":
    main()
