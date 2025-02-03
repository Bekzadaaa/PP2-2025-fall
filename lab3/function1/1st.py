def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams = float(input("Введите количество граммов: "))
ounces = grams_to_ounces(grams)
print(f"{grams} граммов = {ounces} унций")
