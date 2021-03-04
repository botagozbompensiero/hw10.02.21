"""
    params: 1st param: age,
            2nd param :energy
    CATCEMETRY =[]
    len(CATCEMETRY) > 10, = all cats should be deleted

    14. Кіт характеризується життєвою енергією та віком. Кіт може спати, ловити мишу, їсти, тощо (залежить
від фантазії автора класу). Під час цих процесів змінюється життєва енергія та вік кота. Якщо кіт стає
дуже старий або дуже виснажений чи навпаки отримує забагато життєвої енергії, то він уходить в
астрал. Розробити клас, що моделює котів, та написати програму, яка моделює життя деякого кота.
Кіт тепер не уходить в астрал(), а потрапляє на кладовище котів, яке коли повне - "чистять"
Кіт їсть мишу, яка є об'єктом класа миша
В кота є атрибут, що зберігає мишей перед тим як з'їсти
15. Модифікувати клас котів так, щоб кіт мав дев’ять життів і тільки після втрати останнього йшов в
астрал.

Коли котів видалили, щоб була можливість подивитись на їхні  "меморіальні штуки"

в ідеали мати 3 класи
"""


# TODO можно еще добавить трай на ввод age energy и тд чтобы не было отрицательных значений

class Cats:
    """
    max age = 10
    max energy = 10
    min energy = 0
    max lives count = 9
    """

    def __init__(self, name, age=0, energy=5, lives=1):
        self.name = name
        self.age = age
        self.energy = energy
        self.lives_count = lives
        self.mouse_storage = []
        Cats.proverka(self)

    def sleep(self):
        self.energy += 1
        self.age += 1
        return Cats.proverka(self)

    def eat(self):
        self.mouse_storage.append(Mouse.mouse)
        if len(self.mouse_storage) > 2:
            self.mouse_storage.clear()
            self.energy += 1
        return Cats.proverka(self)

    def catch_mouse(self):
        self.age += 1
        self.energy -= 1
        return Cats.proverka(self)

    def proverka(self):
        if self.lives_count < 10:
            if self.age >= 10 or self.energy >= 10 or self.energy == 0:
                self.lives_count += 1
                self.age = 0
                self.energy = 5
        else:
            Cemetery.go_to_astral(self.name)


class Mouse:
    mouse = 'maus'


cemetery = []


class Cemetery:
    # TODO порешать со списком. норм ли, что он вне класса
    @staticmethod
    def go_to_astral(name):
        global cemetery
        cemetery.append(name)
        if len(cemetery) > 5:
            cemetery.clear()
