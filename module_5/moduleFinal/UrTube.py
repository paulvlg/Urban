import time

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, хэш пароля, возраст
    """

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return f"Пользователь: {self.nickname}, возраст: {self.age}"


class Video:
    def __init__(self, title: str, duration: int, adult_mode = bool(False)):
        self.title = title
        self.duration = duration
        self.time_now = 0
        # self.adult_mode = False


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user == nickname and password == user.password:
                self.current_user = user
                return


    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {user} уже существует.')
                return
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
        print(f'Пользователь: {nickname} зарегистрирован и авторизовался в сервисе.')

    def log_out(self):
        self.current_user = None

    def add(self, *args):


    def get_video(self, *args, **kwargs):
        pass

    def watch_video(self, played_video):
        pass


