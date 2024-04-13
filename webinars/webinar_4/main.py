from typing import List
from datetime import datetime


class Car:
    count = 0
    BASE_URL = "https://youtube.com"

    @classmethod
    def count_plus(cls):
        cls.count += 1

    def __init__(self, brand: str, model: str, color: str) -> None:
        self.brand = brand
        self.model = model
        self.color = color
        self.count_plus()
        self.__check_engine()

    def __enter__(self):
        print('Start engine')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Stop engine')

    def __str__(self):
        return f'{self.brand} - {self.model}'

    def __add__(self, other):
        print(self.brand, other.brand)

    @staticmethod
    def __check_engine():
        print('check ok')

    def start(self):
        print('Wruuum')

    # def youtube_get_video(self, video_id, region, func) -> dict:
    #     r = requests.get(self.BASE_URL + f"/get_video?video_id={video_id}&region={region}")
    #     return r.json()


def timer(func):
    def wrapper():
        print(f'start - {datetime.now()}')
        func()
        print(f'end - {datetime.now()}')
    return wrapper

@timer
def test_2():
    for i in range(100000):
        pass

test_2()

cl = Car
a = Car('AUDI', 'Q6', 'red')
b = Car("Rover", '75', 'silver')
c = str(a)

print('stop')
