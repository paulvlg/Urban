def get_decode(number):
    pairs = []
    if number < 3:
        print("Выход без результата")
        return
    for number1 in range(1, number + 1):
        decode = []
        for number2 in range(number1, number + 1):
            if number1 == 1 and  number2 == 1:
                continue
            elif number % (number1 + number2) == 0:
                pairs.append(number1)
                pairs.append(number2)
            decode.append(pairs)
    return (decode)


number = int(input("Введите число от 3 до 20, если менее 3 - выход => "))
result = get_decode(number)
string_result = ''.join(map(str, *result))
print(string_result)
