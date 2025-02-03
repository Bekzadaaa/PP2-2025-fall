set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_set = set_a | set_b
print("Объединение:", union_set)
intersection_set = set_a & set_b
print("Пересечение:", intersection_set)
difference_set = set_a - set_b
print("Разность:", difference_set)
symmetric_difference_set = set_a ^ set_b
print("Симметрическая разность:", symmetric_difference_set)
is_member = 3 in set_a
print("3 принадлежит множеству set_a:", is_member)
set_a.add(7)
print("Множество после добавления 7:", set_a)
set_a.remove(4)
print("Множество после удаления 4:", set_a)
set_length = len(set_a)
print("Длина множества set_a:", set_length)
