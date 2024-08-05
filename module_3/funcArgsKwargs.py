def single_root_words(root="root", *other_words):
    same_words = []
    for i in range(len(other_words)):
        check_root = root.lower()
        check_word = other_words[i].lower()
        if check_root in check_word or check_word in check_root:
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)