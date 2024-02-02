coll = {1000, 1300, 3, 4, 5}  # set
person = {  # dict
    'name': 'kirill',
    'age': 30
}
array_2 = (1, 2, 3, 4, 5)  # tuple

a = "ООО 'Рога и Копыта'"


string = 'Сиротинский Кирилл'  # string
# print("start")
# print(array_1[1::2])


a = 1
b = 2
c = 3
d = int(input("Введите цифру - "))
if d % 3 == 0:
    print("Ваша цифра кратна 3")
elif d % 4 == 0:
    print("Ваша цифра кратна 4")
elif d % 5 == 0:
    print("Ваша цифра кратна 5")
elif d % 6 == 0:
    print("Ваша цифра кратна 6")
else:
    print("Ни одно из условий не отработало")

user = {
    "name": "kirill",
    # 'age': 30,
    "authorized": True
}
array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list
try:
    1 + "1"
except KeyError:
    print('KeyError')
except IndexError:
    print("IndexError")
except:
    print("Произошла ошибка")
finally:
    print("finally")

print('end')
