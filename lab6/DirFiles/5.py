data = ["line1", "line2", "line3"]
file_path = "text.txt"
with open(file_path, 'w') as file:
    file.writelines("\n".join(data))