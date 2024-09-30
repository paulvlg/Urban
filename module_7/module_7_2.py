def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings, start=1):
        strings_positions[i, file.tell()] = string
        file.write(f'{string}\n')
        file.seek(file.tell() + 1)  # offset cursor place but that cheat for Lesson exercise
        # because break output file
    file.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
