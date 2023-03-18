from lesson_2_data import courts, respondents
import requests
from random import randint

BASE_URL = "http://cbr.ru"
a = None

schema_dict = {"name": None,
              "age": None,
              "address": None}

def main(name: str = "kirill", age: int = 29):
    new_dict = schema_dict.copy()
    new_dict["name"] = "kirill"
    new_dict["age"] = 29
    new_dict["address"] = "Moscow"
    return new_dict


if __name__ == "__main__":
    main()
    print("stop")
