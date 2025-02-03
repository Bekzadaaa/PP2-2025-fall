def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]
input = input("Введите слово или предложение: ")
if is_palindrome(input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
