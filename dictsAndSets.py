my_dict = {'Paul' : 1974, 'Elena' : 1977, 'Alexa' : 1998}
print(my_dict,'Это мой словарь')
print(my_dict['Paul'],'Это значение по ключу Paul')
print(my_dict.get('Lena','Ключа с именем Lena в словаре нет'))
my_dict.update({'Lena' : 1978, 'Sasha' : 1974})
print(my_dict, 'Это уже обновленный словарь')
kum = my_dict.pop('Sasha')
print(my_dict, 'Обновленный словарь c выведенным значеним Sasha ', kum)

my_sets = {'3', 'Ace', '3'}
print(my_sets)
my_sets.update('4', '7')
print(my_sets, 'Еще, две')
my_sets.remove('3')
print(my_sets, '"Но не "очко" обычно губит, а к одиннадцати туз"')



