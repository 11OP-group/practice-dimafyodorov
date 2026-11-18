word_list = list(input("Введите слово> ").lower())
word_list_revert = word_list[::-1]

if word_list == word_list_revert:
    print("Это палиндром")
else:
    print("Не палиндром")