class Vehicle:
    __COLOR_VARIANTS = ['White', 'Black', 'Red', 'Green', 'Blue', 'Graphit', 'Yellow', 'Pink']
    #__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, *, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на", new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan(owner='Fedos', model='Toyota Mark II', color='blue', engine_power=500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Grey')
vehicle1.set_color('BlAcK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

