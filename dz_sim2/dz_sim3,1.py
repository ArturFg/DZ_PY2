# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X
# *Пример:*

# 5
#  1 2 3 4 5
#  3
#  -> 1

import random

n = int(input('Enter the number of elements: '))
x = int(input('Enter the number you want to find: '))
array = []
counter = 0

for i in range(0, n - 1):
    array.append(random.randint(1, 9))
    if x == array[i]:
        counter += 1
    if i + 2 == n:
        array.append(i + 2)
print(array)
print(counter)
