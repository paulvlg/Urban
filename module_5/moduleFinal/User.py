class User:
    """
    Класс пользователя, содержащий атрибуты: логин, хэш пароля, возраст
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return f"{self.nickname}"

    def __int__(self):
        return f"{self.age}"

