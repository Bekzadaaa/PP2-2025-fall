fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  if fruit == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  if fruit == "banana":
    continue
  print(fruit)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)