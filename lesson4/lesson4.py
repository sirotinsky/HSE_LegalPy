from datetime import date, datetime
from dadata import Dadata

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

    def set_a_listening_datetime(self, start: datetime, end: datetime, location: str, description: str):
        new_listening = {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "location": location,
            "description": description
        }
        self.listening_datetimes.append(new_listening)
        self.listening_datetimes.sort(key=lambda x: x["start"])

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


def test():
    a = CourtCase("А40-183194/2015")
    a.add_participant("7701272485")
    a.add_participant("7701272485")
    a.add_participant("7701272484")
    a.remove_participant("7701272484")
    a.set_a_listening_datetime(datetime(2022, 2, 2, 15, 30),
                               datetime(2022, 2, 2, 15, 45),
                               "АСГМ зал 8014",
                               "Жалоба на действия АУ")
    a.make_a_decision("Все ок обанкротили, АУ молодец")
    print("stop")


if __name__ == "__main__":
    test()
