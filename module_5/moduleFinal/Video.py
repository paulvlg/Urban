class Video:
    """
    Класс видео файлов, содержащий название, длительность, ограничения по возрасту
    """

    def __init__(self, title: str, duration: int, adult_mode=bool(False)):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title, self.duration, self.adult_mode

    # def __eq__(self, other):
    #     return self.title == other.title

    def __contains__(self, item):
        return item in self.title
