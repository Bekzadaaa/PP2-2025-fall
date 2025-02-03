my_list = [1, 2, 3, "Hello", 3.14]
print(my_list)
print(my_list[0])  
print(my_list[-1]) 
print(my_list[1:4])
my_list[2] = 10
print(my_list)
my_list.append(100)
print(my_list)
my_list.insert(2, "New Element")
print(my_list) 
del my_list[1]
print(my_list)
my_list.remove("Hello")
print(my_list)
last_element = my_list.pop()
print(last_element) 
print(my_list)
list_a = [1, 2]
list_b = [3, 4]
combined_list = list_a + list_b
print(combined_list)
repeated_list = [1, 2] * 3
print(repeated_list) 
