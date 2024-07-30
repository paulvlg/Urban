def count_calls():
    global calls
    calls += 1
    return


def string_info(some_string):
    count_calls()
    len_some_string = len(some_string)
    upper_some_string = some_string.upper()
    lower_some_string = some_string.lower()
    data_some_string = (len_some_string, upper_some_string, lower_some_string)
    return data_some_string


def is_contains(another_string, another_list):
    count_calls()
    lower_another_string = another_string.lower()
    result_compare = any(ele in lower_another_string for ele in another_list)
    return result_compare


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)