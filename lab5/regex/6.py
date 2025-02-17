import re
s = input("Введите строку: ")
result = re.sub(r"[ ,.]", ":", s)
print("Результат:", result)
