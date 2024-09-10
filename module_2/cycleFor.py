#is_prime = True
# С флагом
def primes(args: list):
    primes = []
    not_primes = []
    for i in args:
        is_prime = True
        if i > 1:
            for k in range(2, i):
                if i % k == 0:
                    is_prime = False
            if is_prime:
                primes.append(i)
            else:
                not_primes.append(i)
    return primes, not_primes


#Без флага

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(f'Из списка {numbers}:\nПростые числа - {primes(numbers)[0]}\nНе простые числа - {primes(numbers)[1]}')
# Вариант без флага.
# primes_ = []
# not_primes_ = []
#
# for i in numbers:
#     if i > 1:
#         for k in range(2, i):
#             if i % k == 0:
#                 not_primes_.append(i)
#                 break
#         else:
#             primes_.append(i)
# print(primes_)
# print(not_primes_)

