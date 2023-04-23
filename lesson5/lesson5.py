import time
from random import randint
import hashlib
from collections import deque, Counter
import numpy as np

d1_array = np.array([1, 2, 3, 4])
d2_array = np.array([[1, 2, 3, 4],
                     [1, 2, 3, 4],
                     [1, 2, 3, 4],
                     [1, 2, 3, 4]])
d3_array = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                     [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                     [[1, 2, 3], [1, 2, 3], [1, 2, 3]]])

list_array = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
              [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
              [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]

stack = list()
queue = deque()
print("stop")


def sha_256(text: str):
    a = hashlib.sha256()
    a.update(bytes(text, encoding='utf8'))
    return a.hexdigest()


def hash_demo():
    string_1 = "Дорогие друзья, дальнейшее развитие различных форм деятельности требует от нас анализа дальнейших "
    "направлений развития проекта. Задача организации, в особенности же постоянный количественный "
    "рост и сфера нашей активности представляет собой интересный эксперимент проверки ключевых "
    "компонентов планируемого обновления. Значимость этих проблем настолько очевидна, что рамки и "
    "место обучения кадров способствует подготовке и реализации направлений прогрессивного развития!"
    hash_1 = sha_256(string_1)
    print(f"\n\n\nрезультат выполнения функции - {hash_1}")


def timer(func):
    def wrapper(**kwargs):
        start_time = time.time()
        result = func(**kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"\n{func} --- Выполнена за {duration} секунд")
        return result

    return wrapper


def random_array(**kwargs):
    result = [i for i in range(kwargs['start'], kwargs['limit'], kwargs['step'])]
    return result


@timer
def linear_search(**kwargs) -> bool:
    if kwargs['item'] in kwargs['array']:
        return True
    else:
        return False


@timer
def binary_search(**kwargs) -> bool:
    low = 0
    high = len(kwargs['array']) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = kwargs['array'][mid]
        if guess == kwargs['item']:
            return True
        if guess < kwargs['item']:
            low = mid + 1
        else:
            high = mid - 1
    return False


def task_1():
    start = 1
    limit = 1_000_000
    r_array = random_array(start=start, limit=limit, step=randint(3, 4))
    print(f"Длина массива - {len(r_array)}")
    n_1, n_2, n_3 = randint(start, limit), randint(start, limit), randint(start, limit)
    print(f'Число {n_1} в массиве - {linear_search(array=r_array, item=n_1)}')
    print(f'Число {n_2} в массиве - {linear_search(array=r_array, item=n_2)}')
    print(f'Число {n_3} в массиве - {linear_search(array=r_array, item=n_3)}')
    print(f'Число {n_1} в массиве - {binary_search(array=r_array, item=n_1)}')
    print(f'Число {n_2} в массиве - {binary_search(array=r_array, item=n_2)}')
    print(f'Число {n_3} в массиве - {binary_search(array=r_array, item=n_3)}')


def main():
    # unsorted = [{"name": "Kirill", "age": randint(1, 100000)} for i in range(100000)]
    # unsorted.sort(key=lambda x: x["age"], reverse=True)
    # print("stop")
    # hash_demo()
    task_1()
    pass


if __name__ == "__main__":
    main()
