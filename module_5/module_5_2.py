class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.floors:
            for _ in range(new_floor):
                print(_ + 1)
            return print(f'\nВы прибыли на нужный этаж - {_ + 1}\n')
        else:
            return print(f'Такого этажа ({new_floor}), в доме "{self.name}" - не существует.')

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
