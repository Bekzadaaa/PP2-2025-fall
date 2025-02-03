is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

numbers_input = input("Enter a list of numbers: ")

numbers = list(map(int, numbers_input.split(',')))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)
