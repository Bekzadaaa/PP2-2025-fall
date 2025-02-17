import re
pattern = r"[a-z]+_[a-z]+"
s = input("Введите строку: ")

if re.fullmatch(pattern, s):
    print("Совпадает!")
else:
    print("Не совпадает.")
