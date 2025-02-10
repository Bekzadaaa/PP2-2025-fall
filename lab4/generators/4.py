def squares(a, b):
    for i in range(a, b+1):
        yield i**2
for num in squares(int(input()), int(input())):
    print(num)