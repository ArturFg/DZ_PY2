# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:

# 385916 -> yes
# 123456 -> no

def Sum_Three(num):
    su = 0
    size = 1
    while size <= 3:
        temporary = 0
        temporary = num % 10
        su = su + temporary
        num = num // 10
        size += 1
    return(su, num)
    
h = 1
while h > 0:
    number = int(input('Enter ticket number: ')) 

    if number > 99999 and number < 1000000: 
        sum, number = Sum_Three(number)
        sum2, number = Sum_Three(number)

        if sum == sum2:
            print('Это счистливый белт!!!')
        else:
            print('К сожелению это обычный белет =(')
        h -= 1 
    else:
        print('Некоректно введён номер.')
