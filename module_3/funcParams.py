def print_params(a=1, b='string', c=True):
    print(f'Sending params is: {a}, {b}, {c}')


values_list = [2, 'first_one', 2.1]
values_dict = {'a': 1, 'b': 'Это словарь', 'c': False}
values_list2 = [1.2, 'it is list2']
values_list_2 = [54.32, 'лист 2 из задания']

print_params(2, 'строка', False)
print_params(*values_list)
print_params(**values_dict)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list2)
print_params(*values_list_2, 42)

