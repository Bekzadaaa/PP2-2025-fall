import re
def snake_to_camel(s):
    return "".join(word.capitalize() for word in s.split("_"))

s = input("Введите строку в snake_case: ")
print("CamelCase:", snake_to_camel(s))
