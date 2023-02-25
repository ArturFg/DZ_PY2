# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), 
# не превосходящие числа N.

# Ввод:
# 6
# Вывод
# 1 2 4
# Ввод
# 24
# Вывод
# 1 2 4 8 16

n = int(input('Enter a number: ')) # Пишу на английском, потому что на руском выдоёт ошибку.
deg = 1
degree = []

for i in range(1, n):
    print(deg)
    degree.append(deg)
    deg += deg
    if n <= deg:
        break
print(f'List of all integer powers of two {degree}')
