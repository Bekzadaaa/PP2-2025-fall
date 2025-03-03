import string  

for letter in string.ascii_uppercase:  # Перебираем буквы A-Z  
    with open(f"{letter}.txt", "w") as f:  
        f.write(f"This is {letter}.txt\n")  # Записываем в файл  

