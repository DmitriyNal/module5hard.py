from time import sleep


class User:  # Класс пользователя
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):  # Хэш пароля пользователя
        return hash(password)

    def __repr__(self):
        return f"User(nickname={self.nickname}, age={self.age})"


class Video:  # Класс видео
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube: # Класс платформы UrTube
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):# Логин пользователя и пароль пользователя
        for user in self.users:
            if user.nickname == nickname and user.password == self.hash_password(password):
                self.current_user = user

        print("Неверный логин или пароль")

    def register(self, nickname, password, age):# Регистрация пользователя
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):## Добавление видео в платформу UrTube
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)


    def get_videos(self, search_word):# Поиск видео по КЛЮЧЕВОМУ СЛОВУ
        search_word_lower = search_word.lower()
        return [video.title for video in self.videos if search_word_lower in video.title.lower()]

    def watch_video(self, title):## Просмотр видео на платформе UrTube
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return


        video = next((v for v in self.videos if v.title == title), None)#Поиск по названию видео
        if not video:
            print("Видео не найдено")
            return


        if video.adult_mode and self.current_user.age < 18:# условие для просмотра видео
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return


        for second in range(video.time_now, video.duration):
            print(f"Секунда: {second + 1}")
            sleep(1)

        video.time_now = 0
        print("Конец видео")


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
