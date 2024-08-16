number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")
number3 = input("Введите третье число: ")

variant1 = (number1 == number2)
variant2 = (number1 == number3)
variant3 = (number2 == number3)

if variant1 and variant3:
    print("All 3 numbers equals")
elif variant1 or variant2 or variant3:
    print("Only 2 numbers equals")
else:
    print("Zero 0 equals")

# Или так
# if number1 == number2 and number2 == number3:
#     print("All 3 numbers equals")
# elif number1 == number2 or number1 == number3 or number2 == number3:
#     print("Only 2 numbers equals")
# else:
#     print("Zero 0 equals")
