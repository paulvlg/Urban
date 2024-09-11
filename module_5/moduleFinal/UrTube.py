import time
from module_5.moduleFinal.User import User


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

    def log_out(self):
        self.current_user = None

    def add(self, *films):
        for name_movie in films:
            if name_movie.title not in [video.title for video in self.videos]:
                self.videos.append(name_movie)

    def get_videos(self, text: str):
        movies = []
        [movies.append(video.title) for video in self.videos if text.lower() in video.title.lower()]
        return movies

    def watch_video(self, film: str):
        if self.current_user:
            for video in self.videos:
                if self.current_user and self.current_user.age < 18:
                    print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                if film in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print(f'Конец видео')
        else:
            print(f'Войдите в аккаунт')
