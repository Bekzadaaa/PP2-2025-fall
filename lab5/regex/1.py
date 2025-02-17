import re

pattern = r"ab*"
s = input("Введите строку: ")

if re.fullmatch(pattern, s):
    print("Совпадает!")
else:
    print("Не совпадает.")
