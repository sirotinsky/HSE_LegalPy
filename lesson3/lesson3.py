import json
import csv
import datetime
import decimal
import re

"""
Найдите информацию об организациях:
a. Получите список ИНН из файла «traders.txt»;
b. Найдите информацию об организациях с этими ИНН в файле
«traders.json»;
c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла
«traders.txt» в файл «traders.csv».
"""


def task_1():
    with open("traders.txt", "r") as f:
        inns = [i.rstrip() for i in f.readlines()]
    with open("traders.json", "r") as f:
        traders = [i for i in json.load(f) if i['inn'] in inns]
    with open('traders.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['INN', 'OGRN', 'ADDRESS'])
        for i in traders:
            writer.writerow([i['inn'], i['ogrn'], i['address']])


def task_2():
    with open("100000_efrsb_messages.json", "r") as f:
        msgs = json.load(f)
    email_pattern = re.compile(r'\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+\b')
    results = {}
    for i in msgs:
        emails = re.findall(email_pattern, i['msg_text'])
        for y in emails:
            y = y.lower()
            searched = results.get(i['publisher_inn'])
            if searched and y not in searched:
                results[i['publisher_inn']].append(y)
            elif not searched:
                results.update({i['publisher_inn']: [y]})
            else:
                pass
    with open('emails.json', "w") as f:
        json.dump(results, f)
    print("stop")


def main():
    task_1()
    task_2()


if __name__ == "__main__":
    main()
    print("stop")
