def divides_3_and_4(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
for num in divides_3_and_4(int(input())):
    print(num)    