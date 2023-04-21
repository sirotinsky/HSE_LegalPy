import json
import csv
import re
from ics import Calendar
from datetime import datetime, timedelta
import zoneinfo

zone = zoneinfo.ZoneInfo("Europe/Moscow")


def task_1():
    with open("traders.txt", "r") as f:
        inns = [i.rstrip() for i in f.readlines()]
    with open("traders.json", "r") as f:
        all_traders = json.load(f)
    traders = []
    for trader in all_traders:
        if trader['inn'] in inns:
            traders.append(trader)
    with open('traders.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['INN', 'OGRN', 'ADDRESS'])
        for i in traders:
            writer.writerow([i['inn'], i['ogrn'], i['address']])


email_pattern = re.compile(r'\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')
inn_org_pattern = re.compile(r'\b\d{10}\b')
inn_person_pattern = re.compile(r'\b\d{12}\b')


def task_2():
    with open("10000_efrsb_messages.json", "r") as f:
        msgs = json.load(f)
    results = {}
    for i in msgs:
        emails = re.findall(email_pattern, i['msg_text'])
        for email in emails:
            email = email.lower()
            searched = results.get(i['publisher_inn'])
            if searched and email not in searched:
                results[i['publisher_inn']].append(email)
            elif not searched:
                new_item = {i['publisher_inn']: [email]}
                results.update(new_item)
    inverted = {}
    for inn, emails in results.items():
        for email in emails:
            searched = inverted.get(email)
            if searched and inn not in searched:
                inverted[email].append(inn)
            elif not searched:
                new_item = {email: [inn]}
                inverted.update(new_item)

    with open('emails.json', "w") as f:
        json.dump(results, f)
    print("stop")


def task_3(case_number):
    with open(f"{case_number}.ics", "r") as f:
        raw_data = f.read()
    c = Calendar(raw_data)
    cleaned_events = [i for i in c.events if i.begin.datetime > datetime.now(zone) - timedelta(days=10000)]
    result = [{"case_number": f"{case_number}",
               "start": i.begin.datetime.isoformat(),
               "end": i.end.datetime.isoformat(),
               "location": i.location.strip(),
               "description": i.description
               } for i in cleaned_events]
    with open(f"{case_number}_listenings.json", "w") as f:
        json.dump(result, f)
    return result


def main():
    case_number = "А40-183194-2015"
    # task_1()
    # task_2()
    result = task_3(case_number)


if __name__ == "__main__":
    main()
    print("stop")
