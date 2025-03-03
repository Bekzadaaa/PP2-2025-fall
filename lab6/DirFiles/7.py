with open("text.txt", "r") as orig, open("text2.txt", "w") as Copy:
    Copy.write(orig.read())
