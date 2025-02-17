import re
s = input("Введите строку в CamelCase: ")
result = re.sub(r"([A-Z])", r" \1", s).strip()
print("Результат:", result)
