#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
from pydantic import BaseModel, ValidationError, validator

# Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
# группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия:
# 1. ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# 2. записи должны быть упорядочены по алфавиту;
# 3. вывод на дисплей фамилий и номеров групп для всех студентов, имеющих хотя бы одну оценку 2;
# 4. если таких студентов нет, вывести соответствующее сообщение.


class Student(BaseModel):
    name: str
    group: str
    marks: list

    @validator('marks')
    def amount_of_marks_should_be_5(cls, v: int) -> int:
        if len(v) != 5:
            raise ValueError("marks != 5")
        for i in v:
            if i > 5 or i < 1:
                raise ValueError("wrong marks")
        return v


def add(staff):
    """
    Ввести данные студента в словарь
    """
    name = input("Фамилия и инициалы? ")
    group = input("Номер группы? ")
    buf = [int(a) for a in input().split()]
    lmarks = list(filter(lambda x: 0 < x < 6, buf))
    if len(lmarks) != 5:
        print("ошибка в количестве оценок", file=sys.stderr)
    else:
        student = {
            "name": name,
            "group": group,
            "marks": lmarks,
        }
        staff.append(student)


def show(staff):
    """
    Вывод записей всего словаря
    """
    if staff:
        line = "+-{}-+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 20, "-" * 15)
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^15} |".format(
                "№", "Ф.И.О.", "Группа", "Успеваемость"
            )
        )
        print(line)

        for idx, student in enumerate(staff, 1):
            lmarks = student.get("marks", "")
            print(
                "| {:>4} | {:<30} | {:<20} | {:>15} |".format(
                    idx,
                    student.get("name", ""),
                    student.get("group", ""),
                    " ".join(map(str, lmarks)),
                )
            )
        print(line)
    else:
        print("Список пуст")


def marks(staff):
    """
    Вывод фамилий и номеров групп, студентов имеющих 2
    """
    count = 0
    line = "+-{}-+-{}-+".format("-" * 30, "-" * 10)
    for student in staff:
        if 2 in student.get("marks"):
            count += 1
            if count == 1:
                print(line)
            print(
                "| {:<30} | {:^10} |".format(
                    student.get("name", ""),
                    student.get("group", ""),
                )
            )
            print(line)

    if count == 0:
        print("Студенты не найдены.")


def help():
    print("exit - выход из программы")
    print("add - добавить запись с словарь")
    print("show - показать записи в словаре")
    print("marks - показать у кого 2")
    print("help - помощь")


def save_students(file_name, staff):
    """
    Сохранить всех студентов в файл JSON
    """
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_students(file_name):
    """
    Загрузить всех работников из файла JSON
    """
    with open(file_name, "r", encoding="utf-8") as fin:
        loadfile = json.loads(fin.read())
        try:
            for i in loadfile:
                Student.parse_raw(str(i).replace("'", '"'))
            print("success")
            return loadfile

        except ValidationError as err:
            print("error")
            print(err)
            exit()


def main():
    """
    Главная функция программы
    """
    students = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            add(students)
            if len(students) > 1:
                students.sort(key=lambda item: item.get("name", ""))

        elif command == "show":
            show(students)

        elif command == "marks":
            marks(students)

        elif command == "help":
            help()

        elif command.startswith("save "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]

            save_students(file_name, students)

        elif command.startswith("load "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            students = load_students(file_name)


if __name__ == "__main__":
    main()
