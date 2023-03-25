# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран получившийся кортеж.

# Sample Input:
# house=дом car=машина men=человек tree=дерево

# Sample Output:
# ((house, дом), (car, машина), (men, человек), (tree, дерево))

def creating_a_tuple(word):
    quant = len(word)
    quant = quant // 2
    temporary = [0, 1, 2, 3] # Почему то с циклом аппенд не получается.

    for i in range(quant):
        mirror = (word[i], word[i+1])
        temporary[i] = (mirror)

    return temporary

words = ('house=дом car=машина men=человек tree=дерево')
words = words.replace('=', ' ')
words = words.split(' ')

quantity = len(words)
quantity = quantity // 2

words = creating_a_tuple(words)
# words = map(creating_a_tuple, words) # И map тоже неработает.
print(words)
