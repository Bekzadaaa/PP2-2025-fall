print(14 > 7)
print(14 == 7)
print(14 < 7)

a = 301
b = 201

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y)) 

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

class myclass():
  def __len__(self):
    return 0

ads = myclass()
print(bool(ads)) 

def boolFunction() :
  return True

print(boolFunction())

def boolFunction() :
  return True

if boolFunction():
  print("YES!")
else:
  print("NO!")