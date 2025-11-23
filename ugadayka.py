from random import *


def is_valid(b):
    return b.isdigit() and 1 <= int(b) <= 100


def input_num():
    while True:
        b = input()
        if is_valid(b):
            return int(b)
        else:
            print("Пожалуйста, вводите целые числа\n")


def compare(f_num, s_num):
    num = randint(f_num, s_num)
    count = 0
    while True:
        z = input_num()
        count += 1
        if z < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif z > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif z == num:
            print(f"Вы угадали, поздравляем! Вы пытались угадать число {count} раз!\n")
            count = 0
            break


def new_game():
    ng = input("Хотите сыграть еще? Ответьте д/н \n").lower()
    while True:
        if ng not in ("n", "y", "д", "н"):
            print("Пожалуйста, ответьте 'д' если готовы начать игру, 'н' если нет")
        elif ng in ("n", "н"):
            print("Удачи, и спасибо, что играли в числовую угадайку. Еще увидимся...")
            return False
        else:
            return True


def startgame():
    print("Добро пожаловать! Вы готовы начать игру?")
    while True:
        print("Укажите, в каком диапозоне вы желаете угадывать числа?")
        x, y = input_num(), input_num()
        if x > y:
            x, y = y, x
        print("Введите загаданное число, и узнайте угадали вы или же нет\n")
        compare(x, y)
        if new_game():
            continue
        else:
            break


startgame()
