# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Ввод:
# 7
# 12
# Вывод
# 3 4 или 4 3

x = int(input('Enter: ')) # Данный ввод я сделал для удобства чтобы, неискать подходящие S и P.
y = int(input('Enter: '))

s = x + y
p = x * y

sum = int(s - 1)

for i in range(0, sum):
    for j in range(0, sum):
        r = i * j
        if r == p:
            print(f'Загадонные числа: {i}, {j}.') # По какой то неведомий мне причине, после брейк ещё раз проходится по циклу.
            break
   

