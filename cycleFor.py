numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

#is_prime = True
# С флагом
for i in numbers:
    is_prime = True
    if i > 1:
        for k in range(2, i):
            if i % k == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)
print(primes)
print(not_primes)

# Без флага
# for i in numbers:
#     if i > 1:
#         for k in range(2, i):
#             if i % k == 0:
#                 not_primes.append(i)
#                 break
#         else:
#             primes.append(i)

