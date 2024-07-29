from get_code import get_decode

result_dict = {
                3:'12',
                4:'13',
                5:'1423',
                6:'121524',
                7:'162534',
                8:'13172635',
                9:'1218273645',
                10:'141923283746',
                11:'11029384756',
                12:'12131511124210394857',
                13:'112211310495867',
                14:'1611325212343114105968',
                15:'1214114232133124115106978',
                16:'1317115262143531341251161079',
                17:'11621531441351261171089',
                18:'12151811724272163631545414513612711810',
                19:'118217316415514613712811910',
                20:'13141911923282183731746416515614713812911'}

number = int(input("Введите число от 3 до 20, если менее 3 - выход => "))
result = get_decode(number)
print(f"Результат-Сырец - {result}\n")
string_result = ''.join(map(str, *result))
print(f"Результат приведенный к строке без доп. знаков - {string_result}\n")
check_result = result_dict.get(number) == string_result
print(f"Проверка на результат с условием задачи - {result_dict.get(number)} ==>> {check_result}")
if check_result:
    print("Your bourbon is waiting for you!")
else:
    print("Check it again!")
