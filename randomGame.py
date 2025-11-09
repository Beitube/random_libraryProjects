from random import randint

print("Выберите режим:")
print("Диапазон")
print("Орел и Решка")
choice = input("Ваш выбор: ").lower().strip()


range_mode = ["диапазон", "диапозон"]  
coin_toss = ["орел и решка", "орёл и решка", "орел", "орёл", "решка"]

if choice in range_mode:
    print("Введите границы диапазона:")
    min_limit = int(input("Минимальное значение: "))
    max_limit = int(input("Максимальное значение: "))

    if min_limit >= max_limit:
        print("К сожалению, мы не принимаем такой диапазон")
    else:
        random_number = randint(min_limit, max_limit)
        user_guess = int(input(f"Угадайте число от {min_limit} до {max_limit}: "))

        if user_guess == random_number:
            print(f"Поздравляю! Вы угадали! Загаданное число было {random_number}.")
        else:
            print(f"К сожалению, вы не угадали. Загаданное число было {random_number}.")

elif choice in coin_toss:
    print("Выберите свою сторону:")
    print("1 - Орел")
    print("2 - Решка")
    uchoice = input("Ваш выбор: ").lower().strip()


    userChoice = None
    
    if uchoice in ["орел", "орёл", "1"]:
        userChoice = 1
        choice_name = "Орел"
    elif uchoice in ["решка", "2"]:
        userChoice = 2
        choice_name = "Решка"
    else:
        print("Некорректный выбор!")
        exit()

    orelreshka = randint(1, 2)
    result_name = "Орел" if orelreshka == 1 else "Решка"

    if orelreshka == userChoice:
        print(f"Поздравляю, вы выиграли! Ставка '{choice_name}' оказалась верной!")
    else:
        print(f"К сожалению, ваша ставка '{choice_name}' неверна, выпало '{result_name}'")

else:
    print("Такого режима нет")

