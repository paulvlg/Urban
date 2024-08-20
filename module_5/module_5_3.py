class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        #  Это попытка корявой оптимизации кода, много повторяющихся условий при проверке соответствия типов данных
        #compare_type = isinstance(self.floors, int) or isinstance(House, House)

    def go_to(self, new_floor):
        if 0 < new_floor <= self.floors:
            for _ in range(new_floor):
                print(_ + 1)
            return print(f'\nВы прибыли на нужный этаж - {_ + 1}\n')
        else:
            return print(f'Такого этажа ({new_floor}), в доме "{self.name}" - не существует.')

    # def check_type(compare):
    #     if isinstance(self.floors, int) or isinstance(House, House):
    #         compare_type = True
    #     else:
    #         print('Неверный тип данных')

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.floors}'

    def __eq__(self, other):
        if isinstance(self.floors, int) or isinstance(House, House):
            return self.floors == other
        else:
            print('Неверный тип данных')


    def __lt__(self, other):
        if isinstance(self.floors, int) or isinstance(House, House):
            return self.floors < other
        else:
            print('Неверный тип данных')

    def __le__(self, other):
        if isinstance(self.floors, int) or isinstance(House, House):
            return self.floors <= other
        else:
            print('Неверный тип данных')

    def __gt__(self, other):
        if isinstance(self.floors, int) or isinstance(House, House):
            return self.floors > other
        else:
            print('Неверный тип данных')

    def __ge__(self, other):
        if isinstance(self.floors, int) or isinstance(House, House):
            return self.floors >= other
        else:
            print('Неверный тип данных')

    def __ne__(self, other):
        if isinstance(self.floors, int) or isinstance(House, House):
            return self.floors != other
        else:
            print('Неверный тип данных')

    def __radd__(self, other):
        return House(self.name, self.floors + other)

    def __iadd__(self, other):
        return House(self.name, self.floors + other)

    def __add__(self, value):
        self.floors += value if isinstance(value, int) else print(f'{value} не является целым числом')
        return House(self.name, self.floors)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
