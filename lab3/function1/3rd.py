def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2  # количество кроликов
    x = numheads - y  # количество куриц
    
    return x, y
numheads = int(input("Введите количество голов: "))
numlegs = int(input("Введите количество ног: "))

chickens, rabbits = solve(numheads, numlegs)

print(f"Количество куриц: {chickens}")
print(f"Количество кроликов: {rabbits}")
