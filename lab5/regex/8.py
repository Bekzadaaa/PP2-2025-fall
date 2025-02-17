import re
pattern = r"[A-Z][^A-Z]*"
s = input("Введите строку в CamelCase: ")

matches = re.findall(pattern, s)
print("Разделенные слова:", matches)
