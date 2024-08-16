def calculate_structure_sum(*args):
    total = 0
    for arg in args:
        if isinstance(arg, list):
            for i in arg:
                total += calculate_structure_sum(i)
        elif isinstance(arg, int):
            total += arg
        elif isinstance(arg, dict):
            for key, value in arg.items():
                total += calculate_structure_sum(key, value)
        elif isinstance(arg, set):
            for i in arg:
                total += calculate_structure_sum(i)
        elif isinstance(arg, str):
            total += len(arg)
        elif isinstance(arg, tuple):
            for i in arg:
                total += calculate_structure_sum(i)
    return total


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)