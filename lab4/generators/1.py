def square_generator(N):
    for i in range(N+1):
        yield i**2
for num in square_generator(int(input())):
    print(num)