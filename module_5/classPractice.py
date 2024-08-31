class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
\


if __name__ == '__main__':
    database = Database()
    choice = int(input("Hello!\nYou choice:\n\t1 - Login\n\t2 - Registration\n\tAny else input - Exit"))
    while True:
        if choice == 1:
            login = input("Login: ")
            password = input("Password: ")
            if login in database.data:
                print("You`re logged in")
            else:
                exit("User not find")
        elif choice == 2:
            user = User(input("Input your login: "), password := input("Input your password: "),
                        password2 := input("Confirm your password: "))
            if password != password2:
                print("Password don`t match. Please try again.")
                continue
            database.add_user(user.username, user.password)
            print(database.data)
        else:
            exit('Exit program')
