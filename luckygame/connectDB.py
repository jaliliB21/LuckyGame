import sqlite3


try:
    '''
    Trying to connect to the database and create two user and game tables
    '''
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    # create table users
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # create table games
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT,
        change_box INTEGER,
        score INTEGER,
        total_boxes INTEGER,
        mojeze INTEGER,
        gold_coin INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    # cursor.execute("PRAGMA table_info(games)")
    # columns = cursor.fetchall()
    # for column in columns:
    #     print(column)

    # save the information
    conn.commit()
    # print("ok")

except Exception:
    '''If an exception occurs, the written message is printed'''
    print("not conn")
