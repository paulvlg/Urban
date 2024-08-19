from math import floor

from module_1.variables import name_of_course


class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        if new_floor > self.floors:
            return print(f'Такого этажа ({new_floor}), в доме "{self.name}" - не существует в этом доме.')
        else:
            for _ in range(new_floor):
                print(_ + 1)
        return print(f'\n{_ + 1} - Вы прибыли на нужный этаж\n')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
