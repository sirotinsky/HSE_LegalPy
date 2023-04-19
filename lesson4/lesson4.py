import json
import os
from datetime import date, datetime
from settings import BASE_DIR
import zoneinfo

zone = zoneinfo.ZoneInfo("Europe/Moscow")

"""
При вызове метода конструктора экземпляра (__init__) должны создаваться
следующие атрибуты экземпляра:
● case_number (строка с номером дела — обязательный параметр) передаётся в
качестве аргумента при создании экземпляра
● case_participants (список по умолчанию пустой)
● listening_datetimes (список по умолчанию пустой)
● is_finished (значение по умолчанию False)
● verdict (строка по умолчанию пустая)

У экземпляра должны быть следующие методы:
● set_a_listening_datetime — добавляет в список listening_datetimes судебное
заседание (структуру можете придумать сами)
● add_participant — добавляет участника в список case_participants (можно просто
ИНН)
● remove_participant — убирает участника из списка case_participants
● make_a_decision — вынести решение по делу, добавить verdict и сменить
атрибут is_finished на True
"""


class CourtCase:

    def __init__(self, case_number: str):
        self.case_number = case_number
        self.case_participants = set()
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ""

    def set_a_listening_datetime(self, start: str, end: str, location: str, description: str):
        new_listening = {
            "start": datetime.fromisoformat(start),
            "end": datetime.fromisoformat(end),
            "location": location,
            "description": description
        }
        self.listening_datetimes.append(new_listening)
        self.listening_datetimes.sort(key=lambda x: x["start"], reverse=True)

    def add_participant(self, inn: str):
        if inn not in self.case_participants:
            self.case_participants.update({inn})
        else:
            print("Участник уже есть в деле")

    def remove_participant(self, inn):
        if inn in self.case_participants:
            self.case_participants.remove(inn)
        else:
            print("Такого участника нет в деле")

    def make_a_decision(self, verdict):
        self.verdict = verdict
        self.is_finished = True

    def next_listening(self):
        next_date = None
        for i in self.listening_datetimes:
            if i['start'] < datetime.now(zone):
                break
            next_date = i['start']
        if next_date:
            print(f"Следующее судебное заседание {next_date.isoformat()}")
        else:
            print("Судебных заседаний не намечается")


def test():
    a = CourtCase("А40-183194/2015")
    a.add_participant("7701272485")
    a.add_participant("7701272485")
    a.add_participant("7701272484")
    a.remove_participant("7701272484")
    with open(os.path.join(BASE_DIR, "lesson3", "court_dates.json"), "r") as f:
        dates = json.load(f)
    for i in dates:
        a.set_a_listening_datetime(
            i["start"],
            i["end"],
            i["location"],
            i["description"]
        )
    a.next_listening()
    a.make_a_decision("Все ок обанкротили, АУ молодец")
    print("stop")


if __name__ == "__main__":
    test()
