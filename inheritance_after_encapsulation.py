import random
from encapsulation import Warrior, Mage


class Knight(Warrior):
    def __init__(self, health=100, armor=100, stamina=100):
        super().__init__(health, stamina)
        self.__armor = armor

    def __points_job(self, points):
        if self.__armor > points:
            self.__armor -= points
            print(f'Броня поглощает урон и снижается до {self.__armor}')
            return
        elif self.__armor >= 0:
            if self.__armor != 0:
                print("Броня уничтожена")
            points -= self.__armor
            self.__armor = 0
            super()._set_health(-points)

    def _set_health(self, points):
        if points > 0:
            super()._set_health(points)
        elif points < 0:
            self.__points_job(abs(points))

    def __critical_hit(self, target):
        target._set_health(-10)
        print("----------------")
        print("Критический удар!")
        print(f'{self.__class__.__name__} наносит удар мечом по {target.__class__.__name__}')
        print(f'Здоровье у {target.__class__.__name__} уменьшено до {target._get_health()}')
        print("----------------")

    def attacks(self, target):
        random_number = random.randint(1, 10)
        if random_number <= 4:
            self.__critical_hit(target)
        else:
            super().attacks(target)


class Wizard(Mage):
    def __init__(self, health=60, mana=100, barrier=12):
        super().__init__(health, mana)
        self.__barrier = barrier

    def __points_job(self, points):
        if self.__barrier > points:
            self.__barrier -= points
            print(f'Мгаический барьер поглощает урон и снижается до {self.__barrier}')
            return
        elif self.__barrier >= 0:
            if self.__barrier != 0:
                print("Броня уничтожена")
            points -= self.__barrier
            self.__barrier = 0
            super()._set_health(-points)

    def _set_health(self, points):
        if points > 0:
            super()._set_health(points)
        elif points < 0:
            self.__points_job(abs(points))

    def __critical_hit(self, target):
        target._set_health(-15)
        print("----------------")
        print("Критический удар!")
        print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
        print(f'Здоровье у {target.__class__.__name__} уменьшено до {target._get_health()}')
        print("----------------")

    def attacks(self, target):
        random_number = random.randint(1, 10)
        if random_number >= 8:
            self.__critical_hit(target)
        else:
            super().attacks(target)
