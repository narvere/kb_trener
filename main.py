import random
from datetime import datetime
import time

dictionary = {"r_ukaz_p": ["н", "г", "р", "о", "т", "ь"],
              "l_ukaz_p": ["к", "е", "а", "п", "м", "и"],
              "r_srd_p": ["ш", "л", "б", ],
              "l_srd_p": ["у", "в", "с", ], }
num_words = 10


# num_letters = 14


def target():
    x = round(num_words * 1.5 * 60 / 220, 2)
    print(f"Цель: {x} секунд")
    print("#" * 10)


def intro(key):
    print(f"Сегодня мы работаем с {key}")


def programm(key):
    start_time = datetime.now()
    wrong = 0
    ok = 0
    total = 0
    while total < num_words:
        sign = random.choice(key)
        print(sign)
        answer = input()
        if sign == answer:
            print("OK!")
            ok += 1
        else:
            print("Wrong!")
            wrong += 1
        total += 1
    stop = datetime.now() - start_time
    print(stop)
    print(f"Правильно/неправильно: {ok}/{wrong}")
    ok += 1


def programm2(key, num_letters):
    start_time = datetime.now()
    wrong = 0
    total = 1

    while total <= num_words:
        sign = ""
        for i in range(num_letters):
            sign1 = random.choice(key)
            sign += sign1
        answer = printing(sign, total)
        while sign != answer:
            print("Wrong!")
            answer = printing(sign, total)
            wrong += 1
        print("OK!")
        total += 1
    stop = datetime.now() - start_time
    print(stop)
    print(f"Неправильно: {wrong}")


def printing(sign, total):
    print(total, "-", sign)
    answer = input()
    return answer


def chose_game(x, num_letters):
    intro(x)
    time.sleep(5)
    programm2(x, num_letters)
    # target()


def main():
    while True:
        what = input(
            "Какой палец тренируем?\n* о - правый указательный\n"
            "* а - левый указательный\n* оа - правый и левый указательный\n"
            "* л - правый средний\n")
        if what == 'о':
            chose_game(dictionary['r_ukaz_p'], num_letters=7)

        if what == 'а':
            chose_game(dictionary['l_ukaz_p'], num_letters=7)
        if what == 'оа':
            chose_game(dictionary['r_ukaz_p'] + dictionary['l_ukaz_p'], num_letters=10)
        if what == 'л':
            chose_game(dictionary['r_srd_p'], num_letters=7)
        if what == 'в':
            chose_game(dictionary['l_srd_p'], num_letters=7)
        if what == 'лв':
            chose_game(dictionary['r_srd_p'] + dictionary['l_srd_p'], num_letters=10)


if __name__ == '__main__':
    main()
