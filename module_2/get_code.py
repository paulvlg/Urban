def get_decode(number):
    pairs = []
    if number < 3:
        print("Выход без результата")
        return
    for number1 in range(1, number + 1):
        decode = []

        for number2 in range(number1, number + 1):
            if number % (number1 + number2) == 0 and number1 != number2:
                pairs.append(number1)
                pairs.append(number2)
                continue
            decode.append(pairs)
    return decode
