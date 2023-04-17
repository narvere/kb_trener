import random
import sqlite3
import time
from datetime import datetime

NUM_WORDS = 10
DB_NAME = 'keyboard_trainer.sql3'
TABLE_NAME = 'my_records'

test_branch

def get_saved_time(my_choice):
    """
    Retrieve the saved record time for a given letter from the database.

    Args:
        my_choice (str): The letter to retrieve the saved time for.

    Returns:
        The saved record time as a string, or None if no record is found.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT records FROM {TABLE_NAME} WHERE main_letter = ?;", (my_choice,)
        )
        result = cursor.fetchone()
        return result[0] if result else None


def save_time(my_choice, play_time):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET records = '{str(play_time)}' WHERE main_letter = '{my_choice}';"
        )
        conn.commit()


def update_time(play_time, my_choice):
    """Update the play time for a given letter in the database."""
    # print(str(play_time))
    old_time = get_saved_time(my_choice)
    if old_time is not None and old_time > str(play_time):
    # if old_time > str(play_time):
        print("*" * 20)
        print(f"Поздрвлем! У вас рекорд: {str(play_time)}")
        print("*" * 20)
        save_time(my_choice, play_time)
        # print(old_time, str(play_time))
        # print(f"olen siin ")
    # else:
    #     pass
        # print(old_time, str(play_time))
        #save_time(my_choice, play_time)


def get_letters_list(main_letter):
    """Get the letters list for a given letter from the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT letters_list FROM {TABLE_NAME} WHERE main_letter = ?", (main_letter,)
        )
        finger_one = cursor.fetchall()
        conn.commit()
        return finger_one[0][0]


def get_num_letters(main_letter):
    """Get the number of letters for a given letter from the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT num_letters FROM {TABLE_NAME} WHERE main_letter = ?", (main_letter,)
        )
        finger_one = cursor.fetchall()
        conn.commit()
        return finger_one[0][0]


def def_finger(main_letter):
    """Get the finger for a given letter from the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT finger FROM {TABLE_NAME} WHERE main_letter = ?", (main_letter,)
        )
        finger_one = cursor.fetchall()
        conn.commit()
        return finger_one[0][0]


def get_main_letter():
    """Get all the main letters from the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT main_letter FROM {TABLE_NAME}")
        all_main_letters = cursor.fetchall()
        all_main_letters = [x[0].lower() for x in all_main_letters]
        return all_main_letters


def get_all_fingers():
    """Print out all the fingers and their associated letters."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT main_letter, finger, letters_list, num_letters, records FROM my_records"
        )
        fingers = cursor.fetchall()
        for finger in fingers:
            print(f"* {finger[0]} - {finger[1]} - [{finger[2]}] ({finger[3]} знаков) - {finger[4]}")


def check_input(inp):
    """Checks and modifies user input."""
    try:
        return inp.strip().capitalize()
    except AttributeError as e:
        print(e)


def check_list_input(inp):
    """Checks if input is a list of lowercase letters separated by commas."""
    if inp.isalpha():
        return True
    else:
        return False


def add_new_row(finger, main_letter, letters_list, num_letters):
    """Adds a new row to the database with given parameters."""
    finger = check_input(finger)
    if not check_list_input(letters_list):
        raise ValueError('letters_list must be a list of lowercase letters separated by commas')

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {TABLE_NAME} (finger, main_letter, letters_list, num_letters) VALUES (?, ?, ?, ?)",
                       (finger, main_letter, letters_list, num_letters))
        conn.commit()


def delete_row_by_id(row_id):
    """Deletes a row from the database with the given ID."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?", (row_id,))
        conn.commit()


def get_data_from_db():
    """Retrieves and prints all rows from the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, finger, main_letter, letters_list, num_letters FROM {TABLE_NAME}")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]} - {row[2]}, [{row[3]}], {row[4]}")


def get_user_input(sign, total):
    """Gets user input for the given sign and total."""
    print(f"{total} - {sign}")
    answer = input()
    return answer


def run_program(key, num_letters, my_choice):
    """Runs the program for the given key and number of letters."""
    start_time = datetime.now()
    # wrong = 0
    total = 1

    while total <= NUM_WORDS:
        sign = ''.join(random.choice(key) for _ in range(num_letters))
        answer = get_user_input(sign, total)
        if answer == 'z':
            break
        while sign != answer:
            print("Wrong!")
            answer = get_user_input(sign, total)
            # wrong += 1
        print("OK!")
        total += 1
    stop_time = datetime.now() - start_time
    print()
    print(f"Ваше время {stop_time}\n")
    # sign = ''.join(random.choice(key) for _ in range(num_letters))
    # answer = get_user_input(sign, total)
    if answer != 'z':
        update_time(stop_time, my_choice)
    # print(f"Неправильно: {wrong}")
    print()


def intro(key):
    """Displays an introduction message for the given key."""
    print(f"Сегодня мы работаем с {key}")


def start_game(game_type, my_choice, num_letters):
    """Starts a game for the given game type and number of letters."""
    intro(game_type)
    time.sleep(5)
    run_program(game_type, num_letters, my_choice)
    # target()


def menu():
    """Main function to run the program"""
    while True:
        print("Какой палец тренируем?")
        print("* Б - подключиться к базе данных")
        print("* в - выход из программы")
        print("######################################")
        get_all_fingers()
        print("######################################")
        my_choice = input()
        main_letters = get_main_letter()
        if my_choice == "В":
            print("Exiting program")
            exit()

        elif my_choice in main_letters:
            print(f"{def_finger(my_choice)} - Выход из игры - z")
            # print(get_saved_time(my_choice))
            start_game(list(get_letters_list(my_choice)), my_choice, num_letters=get_num_letters(my_choice))
        elif my_choice == "Б":
            while True:
                print("Вы подключились к базе данных")
                print("д - добавить новую комбинацию в БД")
                print("п - получить данные из БД")
                print("у - удалить данные из БД")
                print("в - вернуться в главное меню")
                second_choice = input()
                if second_choice == "в":
                    break
                if second_choice == "п":
                    get_data_from_db()
                    print()
                if second_choice == "у":
                    row_id = input("Какой ID удалить? ")
                    delete_row_by_id(row_id)
                    print(f"ID {row_id} удален")
                if second_choice == "д":
                    finger = input("Введите название нового объекта (пальца): ")
                    main_letter = input("Укажите программируемую букву: ")
                    letters_list = input("Введите список букв через запятую: ")
                    num_letters = input("Сколько символов будет в слове?: ")
                    add_new_row(finger, main_letter, letters_list, num_letters)
                    print("Новый объект добавлен!")
                else:
                    # Execute script here

                    print(f"Script executed for option {second_choice}")
                    print("* " * 20 + '\n')
                # return second_choice

        # else:
        #     return "Error"


menu()
# print(f"You chose {choice}")
