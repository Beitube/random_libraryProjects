#Вы вводите свой диапазон, и пытаетесь угадать загаданное число между этим диапазоном
from random import randint

print("Введите границы диапазона:")
min_limit = int(input("Минимальное значение: "))
max_limit = int(input("Максимальное значение: "))

if min_limit >= max_limit:
    print("К сожалению, мы не принимаем такой диапозон")
else:

    random_number = randint(min_limit, max_limit)

    user_guess = int(input(f"Угадайте число от {min_limit} до {max_limit}: "))

    if user_guess == random_number:
        print(f"Поздравляю! Вы угадали! Загаданное число было {random_number}.")
    else:
        print(f"К сожалению, вы не угадали. Загаданное число было {random_number}.")

