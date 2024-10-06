import random

user_wins = 0
comp_wins = 0
variants = ["камень", "ножницы", "бумага"]


def user_won():
    global user_wins
    print("Ты выиграл")
    user_wins += 1
    return


def game():
    global user_wins, comp_wins, variants, user_choice
    # 0:Камень, 1: ножницы, 2: бумага

    random_number = random.randint(0, 2)
    computer_pick = variants[random_number]

    print("Компьютер выбрал - ", computer_pick + ".")

    if user_choice == computer_pick:
        print("Снова по новой")
        return user_wins, comp_wins
    elif user_choice == "камень" and computer_pick == "ножницы":
        user_won()
    elif user_choice == "ножницы" and computer_pick == "бумага":
        user_won()
    elif user_choice == "бумага" and computer_pick == "камень":
        user_won()
    else:
        print("Компьютер выиграл")
        comp_wins += 1
    return user_wins, comp_wins


print("Да начнется Игра!")
while True:
    user_choice = input(str("Сделай свой выбор из 'Камень', 'Ножницы', 'Бумага' или"
                            " '0 (ноль)' для выхода из игры\n")).lower()
    if user_choice == '0':
        print("До встречи!")
        break

    if user_choice in variants:
        game()


print("Ты выиграл - %d" % user_wins)
print("Компьютер выиграл - {}".format(comp_wins))
