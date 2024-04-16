import time
from random import randint


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
    limit = 1_000_0000
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


if __name__ == '__main__':
    main()
