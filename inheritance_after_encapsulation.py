from random import randint, choice
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
        random_number = randint(1, 10)
        if random_number <= 4:
            self.__critical_hit(target)
        else:
            super().attacks(target)


class Wizard(Mage):
    def __init__(self, health=60, mana=100, barrier=12):
        super().__init__(health, mana)
        self._barrier = barrier

    def __points_job(self, points):
        if self._barrier > points:
            self._barrier -= points
            print(f'Магический барьер поглощает урон и снижается до {self._barrier}')
            return
        elif self._barrier >= 0:
            if self._barrier != 0:
                print("Броня уничтожена")
            points -= self._barrier
            self._barrier = 0
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
        random_number = randint(1, 10)
        if random_number >= 8:
            self.__critical_hit(target)
        else:
            super().attacks(target)

unit1 = Warrior(100, 100)
unit2 = Mage(60, 100)
unit3 = Knight(100, 100, 100)
unit4 = Wizard(60, 100, 50)

def fight(unit1, unit2, unit3, unit4):
    while True:
        if unit1._get_health() > 0 and unit2._get_health() > 0 and unit3._get_health() > 0 and unit4._get_health() > 0:
            unit1.attacks(choice([unit2, unit3, unit4]))
            unit2.attacks(choice([unit1, unit3, unit4]))
            unit3.attacks(choice([unit1, unit2, unit4]))
            unit4.attacks(choice([unit1, unit2, unit3]))
            if unit1._get_health() <= 0:
                print(f'{unit1.__class__.__name__} is dead')
            elif unit2._get_health() <= 0:
                print(f'{unit2.__class__.__name__} is dead')
            elif unit3._get_health() <= 0:
                print(f'{unit3.__class__.__name__} is dead')
            elif unit4._get_health() <= 0:
                print(f'{unit4.__class__.__name__} is dead')


f = fight(unit1, unit2, unit3, unit4)
print(f)


