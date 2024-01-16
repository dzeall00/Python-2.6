#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Использовать словарь, содержащий следующие ключи: название начального пункта маршрута; 
# название конечного пункта маршрута; номер маршрута. # Написать программу, выполняющую следующие действия: 
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи 
# должны быть упорядочены по номерам маршрутов; вывод на экран информации о маршруте, 
# номер которого введен с клавиатуры; если таких 
# маршрутов нет, выдать на дисплей соответствующее сообщение.


import bisect
import re
import sys


if __name__ == "__main__":
    routes = []
    while True:
        command = input(">>> ").lower()
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        text = (
            '| {:^30} | {:^20} | {:^8} |'.format(
                "Начало",
                "Конец",
                "Номер"
            )
        )

        if command == 'exit':
            break

        elif command == 'add':

            start = input("Введите начальный пункт: ")
            end = input("Введите конечный пункт: ")
            count = int(input("Введите номер маршрута: "))

            route = {
                'начальный пункт': start,
                'конечный пункт': end,
                'номер маршрута': count
            }

            if route not in routes:
                bisect.insort(
                    routes, route, key=lambda item: item.get('номер маршрута'))
            else:
                print("данный маршрут уже добавлен")

        elif command == 'list':
            print(line)
            print(text)
            print(line)
            for route in routes:
                print(
                    '| {:<30} | {:<20} | {:>8} |'.format(
                        route.get('начальный пункт', ''),
                        route.get('конечный пункт', ''),
                        route.get('номер маршрута', '')
                    )
                )

            print(line)

        elif (m := re.match(r'select (.+)', command)):
            name_punct = m.group(1)
            found = False
            for route in routes:
                if str(route['номер маршрута']) == name_punct:
                    if not found:
                        print(line)
                        print(text)
                        print(line)

                    print(
                        '| {:<30} | {:<20} | {:>8} |'.format(
                            route.get('начальный пункт', ''),
                            route.get('конечный пункт', ''),
                            route.get('номер маршрута', '')
                        )
                    )
                    found = True
            if not found:
                print("Маршрутов с данным номером не найдено.")
            else:
                print(line)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("select <номер маршрута> - запросить маршруты, которые имеют данный номер")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
