import calendar
import smtplib
import re
from dadata import Dadata

from decimal import Decimal
from datetime import datetime, date, time, timedelta
import os
import json

print('stop')

working_dir = os.getcwd()
base_dir = os.path.dirname(__file__)

path_1 = '100000_efrsb_messages.json'
path_1_full = os.path.join(base_dir, path_1)
path_2 = 'traders.txt'
path_3 = 'traders.json'



traders_data = json.load(open(path_3, 'r'))

traders_inn = open(path_2, 'r')


a = datetime.now()
b = datetime(2022,2,12,12,12,12)
d = date(2030, 3,3)
f = time(12,12,12)
c = a - b

decimal_1 = Decimal('0.1')
decimal_2 = Decimal('0.2')

print(decimal_1+decimal_2)
print(0.1 + 0.2)

g = a + timedelta(days=10)

def open_data():
    with open(path_1, 'r') as f:
        json_data = json.load(f)

    return json_data


def main():
    data = open_data()
    email_pattern = re.compile(r'\b[0-9a-zA-Z.-_-]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')
    inn_org_pattern = re.compile(r'\b\d{10}\b')
    inn_person_pattern = re.compile(r'\b\d{12}\b')
    email_map = {}
    for i in data:
        temp = re.findall(email_pattern, i.__str__())
        if email_map.get(i['publisher_inn']):
            email_map[i['publisher_inn']] += temp
        else:
            email_map[i['publisher_inn']] = temp
        email_map[i['publisher_inn']] = list(set(email_map[i['publisher_inn']]))
        print('stop')
    print('final stop')

ddt = Dadata('340e9972893243b9ef326fb473a3fb3b2ccf3bdd',
             '5a78e67c65c44d1051aed5f3e51e9f9014ea7bdc')

print('stop')

if __name__ == "__main__":
    main()