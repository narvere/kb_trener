import random
from datetime import datetime
import time

# Define a dictionary of keys and their corresponding letters
dictionary = {"r_ukaz_p": ["н", "г", "р", "о", "т", "ь"],
              "l_ukaz_p": ["к", "е", "а", "п", "м", "и"],
              "r_srd_p": ["ш", "л", "б", ],
              "l_srd_p": ["у", "в", "с", ], }
num_words = 10


# num_letters = 14

# def write_db_file(best_time, finger):
#     with open('filename.txt', 'w', encoding='utf-8') as f:
#         f.write(f'Лучшее время {finger} - {best_time}\\n')
#         f.write(f'Лучшее время {finger} - {best_time}\\n')
#         print(f"File updated! - {best_time}")


def target():
    """Calculate and display the target time for the user"""
    x = round(num_words * 1.5 * 60 / 220, 2)
    print(f"Цель: {x} секунд")
    print("#" * 10)


def intro(key):
    """Display an introduction message for the given key"""
    print(f"Сегодня мы работаем с {key}")


def program(key):
    """Run the program for the given key"""
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
    # write_db_file(stop)
    print(f"Правильно/неправильно: {ok}/{wrong}")


def run_program(key, num_letters, finger):
    """Run the program for the given key and number of letters"""
    start_time = datetime.now()
    wrong = 0
    total = 1

    while total <= num_words:
        sign = ''.join(random.choice(key) for _ in range(num_letters))
        answer = get_user_input(sign, total)
        while sign != answer:
            print("Wrong!")
            answer = get_user_input(sign, total)
            wrong += 1
        print("OK!")
        total += 1
    stop = datetime.now() - start_time
    print(stop)
    # write_db_file(stop, finger)
    print(f"Неправильно: {wrong}")


def get_user_input(sign, total):
    """Get user input for the given sign and total"""
    print(f"{total} - {sign}")
    answer = input()
    return answer


def start_game(game_type, num_letters, finger):
    """Start a game for the given game type and number of letters"""
    intro(game_type)
    time.sleep(5)
    run_program(game_type, num_letters, finger)
    # target()


def main():
    """Main function to run the program"""
    finger_dict = {
        'о': ('r_ukaz_p', 7, 'правый указательный'),
        'а': ('l_ukaz_p', 7, 'левый указательный'),
        'оа': ('r_ukaz_p' + 'l_ukaz_p', 10),
        'л': ('r_srd_p', 7),
        'в': ('l_srd_p', 7),
        'лв': ('r_srd_p' + 'l_srd_p', 10)
    }
    menu(finger_dict)


def menu(finger_dict):
    while True:
        what = input(
            f"Какой палец тренируем?\n"
            f"* Б - подключиться к базе данных\n######################################\n* о - {finger_dict['о'][2]}\n"
            f"* а - {finger_dict['а'][2]}\n-----\n* оа - правый и левый указательный\n"
            "* л - правый средний\n######################################\n")
        if what != 'Б':
            if what in finger_dict:
                print(finger_dict[what][2])
                start_game(dictionary[finger_dict[what][0]], finger=finger_dict[what][2],
                           num_letters=finger_dict[what][1])
        elif what == 'Б':
            print("Вы подключились к базе данных")
            combination = input(
                f"д - добавить новую комбинацию в БД\n"
                f"п - получить данные из БД\n"
                f"у - удалить данные из БД\n"
                f"в - вернуться в главное меню\n"
            )
            if what == 'в':
                menu(finger_dict)
            break


if __name__ == '__main__':
    main()
