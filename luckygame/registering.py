import hashlib
import time
from connector import saver

from connectDB import cursor, conn
from luckygame import LuckyGame
from prettytable import PrettyTable


# add to version 3.0.1
table1 = PrettyTable()
table1.field_names = ["ID", "Name"]
table2 = PrettyTable()
table2.field_names = ["ID", "Name", "Count GoldCoin", "Change Box", "Score", "Count Opened Boxes", "Count Mojeze"]


def add_game(user_id: int, name: str) -> None:
    """
    This function creates an instance of the Lucky Game class and stores them in the games table, then calls the saver
    function from the connector module.

    :param user_id:
    :param name:
    :return:
    The return value of this call is the user_menu function.
    """

    sample = LuckyGame(user_id, name)
    cursor.execute('''INSERT INTO games (user_id, name, change_box, score, total_boxes, mojeze, gold_coin) 
                VALUES (?, ?, ?, ?, ?, ?, ? )''', (sample.user_id, sample.name, sample.myChangeBox,
                                                   sample.myScore, sample.total_boxes, sample.mojeze, sample.GoldCoin))
    conn.commit()
    print("start game to 3 seconds☺")
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    saver(user_id, sample)
    sample.starter()

    return user_menu(user_id)


def show_user_games(user_id: int) -> None:
    """
    This function displays the games created by the user.
    :param user_id:
    :return: None
    """
    cursor.execute("SELECT id, name, change_box, score, total_boxes, mojeze, gold_coin FROM games WHERE user_id = ?",
                   (user_id,))
    games = cursor.fetchall()

    if games:
        print("your games: ")
        table1.clear_rows()
        for game in games:
            # print(game)
            # edit to version 3.0.1
            table1.add_row([game[0], game[1]])
        print(table1)
        question = input("your show detail game clicked ID Number (i'm not show detail: exit): ")
        if question == "exit":
            user_menu(user_id)

        else:
            for game in games:
                if game[0] == int(question):
                    # edit to version 3.0.1
                    table2.clear_rows()
                    table2.add_row([game[0], game[1], game[6], game[2], game[3], game[4], game[5]])
                    print(table2)

            question = input("back list games? (yes: list games)(no type: user menu) : ")
            if question == "yes":
                show_user_games(user_id)

    else:
        print("not any games")


def user_menu(user_id: int) -> None:
    """
    A user interface menu appears that provides the following features:
    1- show all games user
    2- create new game
    3- logout user
    :param user_id:
    :return: None
    """
    while True:
        choice = input("(choice: 1:show all games, 2:create game, 3:logout) : ")

        if choice == '1':
            # show user games
            show_user_games(user_id)

        elif choice == '2':
            # create new game
            name = input("your game is name: ")
            add_game(user_id, name)

        elif choice == '3':
            print("logout success")
            break
        continue


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def sign_up(username, password):
    password_hashed = hash_password(password)

    # The user selection is entered with username
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    #
    user = cursor.fetchone()

    if user:
        print("username not unavailable")
        return False
    else:
        # Creates a new user
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hashed))
        conn.commit()

        print("register successfully")
        return True


def login(username, password):
    password_hashed = hash_password(password)

    # Selecting a user with this username and password from the database
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password_hashed))
    user = cursor.fetchone()

    if user:
        print("login successful")
        user_id = user[0]

        user_menu(user_id)
        return True
    else:
        print("username or password available")
        return False
