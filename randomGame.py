from random import randint

print(
    "Выберите режим: \nДиапазон \nОрел и Решка \nКамень Ножницы бумага \nКости \nКубики \nЧет-Нечет \nРусская рулетка \nВаш выбор: "
)
choice = input().lower().strip()


range_mode = ["диапазон", "диапозон"]
coin_toss = ["орел и решка", "орёл и решка", "орел", "орёл", "решка"]
rock_scissors_paper = ["камень", "ножницы", "бумага"]
bones = ["кости"]
cubes = ["кубики"]
rulette = [
    "чет-нечет",
    "чет нечет",
    "чёт-нечет",
    "чёт нечет",
    "чёт-нечёт",
    "чёт нечёт",
    "чет-нечёт",
    "чет нечёт",
    "чет",
    "чёт",
    "нечет",
    "нечёт",
]
rusrulette = ["русская рулетка", "рулетка"]

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
        print(
            f"К сожалению, ваша ставка '{choice_name}' неверна, выпало '{result_name}'"
        )

elif choice in rock_scissors_paper:
    print("Выберите свой вариант:")
    print("1 - Камень")
    print("2 - Ножницы")
    print("3 - Бумага")
    uchoice = input("Ваш выбор: ").lower().strip()

    variants = ["камень", "ножницы", "бумага"]
    compIndex = randint(0, 2)
    compChoice = variants[compIndex]

    if uchoice in ["камень", "1"]:
        userIndex = 0
        choice_name = "Камень"
    elif uchoice in ["ножницы", "2"]:
        userIndex = 1
        choice_name = "Ножницы"
    elif uchoice in ["бумага", "3"]:
        userIndex = 2
        choice_name = "Бумага"
    else:
        print("Некорректный выбор!")
        exit()

    if userIndex == compIndex:
        print("Ничья!")
    elif (userIndex - compIndex) % 3 == 1:
        print(f"Компьютер выиграл!, компьютер выбрал: {compChoice}")
    else:
        print("Вы выиграли, поздравляю")

    print(f"Компьютер выбрал {compChoice}")

elif choice in bones:

    usCh = int(input(print("Сколько кубиков хотите бросить?")))

    if usCh <= 0:
        print("Ошибка")
    else:
        rand = randint(1, usCh * 6)

        userChoice = int(
            input(
                print(
                    f"Введите число которое по вашему мнению выпадет на костях, от 1 до {usCh * 6}:"
                )
            )
        )

        if userChoice > usCh * 6 or userChoice <= 0:
            print("Ошибка")
        else:
            if userChoice == rand:
                print(f"Поздравляю! Вы угадали! Число на костях было {rand}.")
            else:
                print(f"К сожалению, вы не угадали. Число на костях было {rand}.")

elif choice in cubes:
    usCh = int(input(print("Сколько кубиков хотите бросить?")))

    if usCh <= 0:
        print("Ошибка")
    else:
        rand = randint(1, usCh * 6)

        print(f"На кубиках в количестве {usCh}, выпало число {rand}")

elif choice in rulette:
    usCh = input("На что вы хотите поставить, чет или нечет?\n").lower()

    rand = randint(1, 36)

    if rand % 2 == 0 and usCh in ("чет", "чёт"):
        print(
            f"Поздравляю, вы выиграли! Число оказалось четным! Выпавшее число: {rand}"
        )
    elif rand % 2 != 0 and usCh in ("нечет", "нечёт"):
        print(
            f"Поздравляю, вы выиграли! Число оказалось нечетным! Выпавшее число: {rand}"
        )
    else:
        print(f"К сожалению, вы проиграли, число было {rand}")

elif choice in rusrulette:
    bullets = [False] * 6
    rand = randint(0, 5)
    bullets[rand] = True

    curchable = 0
    gameover = False

    while curchable < 6 and not gameover:
        print(f"Ход {curchable + 1}, приготовтесь!\n")
        print("Что вы выберите: 1 - стрелять в себя; 2 - стрелять в компьютер\n")

        action = input("Ваш выбор: ").strip()

        if action == "1":
            if bullets[curchable]:
                print("Прогремел выстрел! Вы проиграли...")
                gameover = True
            else:
                print("Щелчок, выстрела не последовало...")
                curchable += 1
        elif action == "2":
            if bullets[curchable]:
                print("Прогремел выстрел! Компьютер проиграл!")
                gameover = True
            else:
                print("Щелчок, выстрела не последовало...")
                curchable += 1
        else:
            print("Такого выбора нет")
else:
    print("Такого режима нет")
