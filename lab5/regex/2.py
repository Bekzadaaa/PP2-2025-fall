import re
pattern = r"ab{2,3}"
s = input("Введите строку: ")

if re.fullmatch(pattern, s):
    print("Совпадает!")
else:
    print("Не совпадает.")
