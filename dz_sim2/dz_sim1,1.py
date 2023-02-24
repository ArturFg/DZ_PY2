# git remote add origin https://github.com/ArturFg/DZ_PY2.git
# git branch -M main
# git push-u origin main

# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Enter a number: '))
sum = 0

if number < 100 and number > 999:
    while number > 9:
        temporary = 0
        temporary = number % 10
        sum = sum + temporary
        number = number // 10

    sum = sum + number
    print(f'Сумма сыфр числа: {sum}.')
else:
    print('Ошибка! введите трёхзначное число.')


# number = int(input('Enter a number: ')) # И вариант без ифа.
# sum = 0

# while number > 9:
#     temporary = 0
#     temporary = number % 10
#     sum = sum + temporary
#     number = number // 10

# sum = sum + number
# print(f'Сумма сыфр числа: {sum}.')