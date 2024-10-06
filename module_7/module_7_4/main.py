import random

user_wins = 0
comp_wins = 0

options = ["камень", "ножницы", "бумага"]

print("Да начнется Игра!")
while True:
    user_input = input(str("Сделай свой выбор из 'Камень', 'Ножницы', 'Бумага' или"
                           " '0 (ноль)' для выхода из игры\n")).lower()
    if user_input == '0':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # 0:Камень, 1: ножницы, 2: бумага

    computer_pick = options[random_number]
    print("Компьютер выкинул", computer_pick + ".")

    if user_input == computer_pick:
        print("Снова по новой")
        continue
    elif user_input == "камень" and computer_pick == "ножницы":
        print("Ты выиграл")
        user_wins += 1
    elif user_input == "ножницы" and computer_pick == "бумага":
        print("Ты выиграл")
        user_wins += 1
    elif user_input == "бумага" and computer_pick == "камень":
        print("Ты выиграл")
        user_wins += 1
    else:
        print("Компьютер выиграл")
        comp_wins += 1

print("Ты выиграл - %d" % user_wins)
print("Компьютер выиграл - {}". format(comp_wins))

