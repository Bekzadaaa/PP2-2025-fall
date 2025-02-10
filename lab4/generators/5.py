def down(n):
    for i in range(n,-1,-1):
        yield i
for num in down(int(input())):
    print(num)