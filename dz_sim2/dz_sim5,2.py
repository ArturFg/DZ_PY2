# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4
def exponentiation(aa, bb):
    if bb == 0:
        return aa
    bb -= 1
    aa += 1
    return exponentiation(aa, bb)
a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
a = exponentiation(a, b)
print(a)