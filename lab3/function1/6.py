def reverse_words():
    user_input = input("Введите строку: ")
    words = user_input.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
result = reverse_words()
print("Перевернутая строка:", result)
