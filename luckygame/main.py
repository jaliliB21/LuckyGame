from registering import sign_up, login
from validation import validate_username, validate_password

while True:
    '''
    This loop provides the main flow of the game.

    - After receiving the user name and password, he registers or enters the user in the system.
    '''
    choice = input("choose: 1:sin up, 2:login, 3:exit: ")

    if choice == '1':
        # edit to version 3.0.1 and 3.1

        while True:
            username = input("username: ")
            password = input("password: ")
            validate_username(username)
            if not validate_username(username):
                print("Username must be between 3 and 10 characters.")

            if not validate_password(password):
                continue
            if sign_up(username, password):
                break


    elif choice == '2':
        # edit to version 3.0.1
        while True:
            username = input("username: ")
            password = input("password: ")

            # login - If the login is successful, the loop will break
            if login(username, password):
                break
        break

    elif choice == '3':
        print("exits")
        break

# behzad jalili
