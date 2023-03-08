# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую неотрицательную степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
def exponentiation(aa, bb, degree):
    if bb == 0:
        return degree
    bb -= 1
    degree *= aa
    return exponentiation(aa, bb, degree)
a = int(input('Enter the number you want to raise to a power: '))
b = int(input('Enter degree: '))
b -= 1
total = a
total = exponentiation(a, b, total)
print(total)