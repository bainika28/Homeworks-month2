import random


def play_game(min_number, max_number, attempts, capital):
    print(f"Начальный капитал: {capital}")
    for attempt in range(attempts):
        print(f"\nПопытка {attempt + 1} из {attempts}")

        while True:
            try:
                bet = float(input(f"Сделайте ставку (ваш капитал {capital}): "))
                if bet <= 0 or bet > capital:
                    raise ValueError("Ставка должна быть больше 0 и меньше или равна вашему капиталу.")
                break
            except ValueError as e:
                print(e)

        number = random.randint(min_number, max_number)
        guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))

        if guess == number:
            print(f"Поздравляем! Вы угадали число {number}. Ваша ставка удваивается!")
            capital += bet
        else:
            print(f"Увы, вы не угадали. Загаданное число было {number}. Ваша ставка теряется.")
            capital -= bet

        if capital <= 0:
            print("Вы исчерпали весь капитал. Игра окончена!")
            break

    return capital