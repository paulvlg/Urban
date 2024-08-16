import math
def divide(first, second):
    if second == 0:
        res_ = f'Делитель равен {second} - {math.inf}'
    else:
        res_ = f'Результат деления: - {first / second}'
    return res_
