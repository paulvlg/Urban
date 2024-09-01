class User:
    """
    Класс пользователя, содержащий атрибуты: логин, хэш пароля, возраст
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __hash__(self):
        return hash(self.password)


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, nickname, password):
        self.data[nickname] = password
