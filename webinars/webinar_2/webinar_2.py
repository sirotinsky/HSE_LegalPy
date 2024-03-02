from pandas import DataFrame
from lesson_2_data import courts, respondents


df = DataFrame()
print("stop")
array = [1, 2, 3, 4, 5, 6, 7, 8]
tuple_ = (1, 2, 3, 4, 5, 6, 7, 8)
person = {
    'name': 'Кирилл',
    'age': 30,
    "authorized": True
}

inn = '7701272485'

for i in array:
    print('вошли в тело цикла')
    print(i)

for k, v in person.items():
    print(k, v)

for i in range(1000):
    if i % 5 == 0:
        print(i)
    elif i % 19 == 0:
        continue
    elif i % 199 == 0:
        break
    print('iter end')

for i, char in enumerate(inn):
    print(i, char)

a = 0
b = 10
while a < b:
    print(a)
    a += 1

array = ['2312', '123123', '1223', '1sdae', 'efsd', '1231']
new_list = [int(i) for i in array if i.isdigit()]
new_dict = {i: 1 for i in array}
print(new_dict)

a = 10


def beautiful_court(court: dict) -> str:
    """
    Функция создает красивый формат для данных о судах

    :param respondent: Словарь с данными арбитражного суда
    :return: Красивая строка с данными арбитражного суда
    """
    new_string = f'В {court["short_name"]}\n' \
                 f'Адрес: {court["address"]}\n\n'
    return new_string


def beautiful_respondent(respondent: dict) -> str:
    """
    Функция создает красивый формат для участника дела

    :param respondent: Словарь с данными ответчика
    :return: Красивая строка с данными ответчика
    """
    new_string = f'Наименование: {respondent["short_name"]}\n' \
                 f'ИНН: {respondent["inn"]}\n' \
                 f'ОГРН: {respondent["ogrn"]}\n' \
                 f'Адрес: {respondent["address"]}\n\n'
    return new_string


def test_func(**kwargs):
    """
    Docstring
    :param name:
    :param surname:
    :return:
    """
    new_string = f'Name: {kwargs["name"]}\n' \
                 f'Surname: {kwargs["surname"]}\n'
    return new_string

def print_respondents():
    for i in respondents:
        new_respondent_str = beautiful_respondent(i)
        print(new_respondent_str, 'asd', 'asdasdasd')

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    number = 45
    # print_respondents()
    new_number = test_func(name='kirill', surname='sirotinsky', age=30)
    print('stop')


if __name__ == '__main__':
    main()
