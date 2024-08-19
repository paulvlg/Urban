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

    def __len__(self):
        return self.floors

    def __str__(self):
        return self.name

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
