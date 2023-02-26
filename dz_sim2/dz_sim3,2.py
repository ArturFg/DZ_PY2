# Задача 18: 
# Требуется найти в массиве из случайных чисел (от 1 до n) 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X
# Пример:

# 5
#  1 2 3 4 5
#  6
#  -> 5

import random

n = int(input('Enter the number of elements: '))
x = int(input('Enter the number you want to find: '))
array = []
difference = 0
place = 0

for i in range(0, n):
    time_difference = 0
    array.append(random.randint(1, n))
    if array[i] == x:
        place = i
        break
    else:
        if i == 0:
            if array[i] > x:
                difference = array[i] - x
                place = i
            else:
                difference = x - array[i]
                place = i
        else:
            if array[i] > x:
                time_difference = array[i] - x
                if time_difference < difference:
                    difference = time_difference
                    place = i
            else:
                time_difference = x - array[i]
                if time_difference < difference:
                    difference = time_difference
                    place = i
print(array)
print(f'{array[place]}, {place}')
