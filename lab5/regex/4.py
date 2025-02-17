import re
pattern = r"[A-Z][a-z]+"
s = input("Введите строку: ")

if re.fullmatch(pattern, s):
    print("Совпадает!")
else:
    print("Не совпадает.")
