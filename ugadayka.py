from random import *

a = randint(1, 100)
print("Добро пожаловать в числовую угадайку \nВведите число от 1 до 100:\n")


def is_valid(b):
    return b.isdigit() and 1 <= int(b) <= 100


def is_valid_num():
    while True:
        b = input("")
        if is_valid(b):
            return int(b)
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")


def compare():
    while True:
        z = is_valid_num()
        if z < a:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif z > a:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif z == a:
            print("Вы угадали, поздравляем!")
            break


compare()

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
