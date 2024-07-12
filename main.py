class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} ест")

    def sing(self):
        print(f"{self.name} поет - Чирик")

    def info(self):
        print(f"Имя - {self.name}, окрас - {self.color}, голос - {self.voice}")


class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name} поет - Курлык курлык")

    def walk(self):
        print(f"{self.name} гуляет")


bird1 = Pigeon("Гоша", "Курлык", "Серый", "Хлебные крошки")
bird2 = Bird("Маша", "Чирик", "Коричневый")

bird1.sing()
bird1.info()
bird1.walk()
