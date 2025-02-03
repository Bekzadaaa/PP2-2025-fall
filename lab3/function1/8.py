def contains_007(nums):
    sequence = [0, 0, 7]
    index = 0  
    for num in nums:
        if num == sequence[index]:
            index += 1  
        if index == len(sequence): 
            return True

    return False
numbers = list(map(int, input("Введите список чисел: ").split()))

print(contains_007(numbers))
