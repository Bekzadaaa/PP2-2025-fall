import re
pattern = r"a.*b"
s = input("Введите строку: ")

if re.fullmatch(pattern, s):
    print("Совпадает!")
else:
    print("Не совпадает.")
