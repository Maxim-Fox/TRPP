# Написать функцию strong_number(number), которая определяет является ли число сильным.
# Число сильное, если сумма факториалов цифр числа равна самому числу.
#
# Примеры:
# strong_number(145) => True -> 1! + 4! + 5! = 1 + 24 + 120 = 145

import traceback


def strong_number(number):
    number2 = number            #"Отзеркаливаем" наше число в переменную number2, чтобы работать с ним
    k = 0
    summa = 0
    while (number2 > 0):        #Узнаем длину нашего числа
        k = k + 1
        number2 = number2 // 10
    number2 = number
    for i in range(0,k):        #Цикл находит сумму факториалов цифр числа, считать начинаем с последнего числа
        c = number2 % 10        #"Отрезаем" последнюю цифру числа
        number2 = number2 // 10 #Сохраняем число без "хвоста"
        factorial = 1           
        while c > 1:            #Находим факториал "хвоста"
            factorial *= c
            c -= 1
        summa += factorial     #Найденный факториал прибавляем к сумме
    if (summa == number):      #Проверяем - наше число сильное или нет?
        return True
    else:
        return False


# Тесты
try:
    assert strong_number(1) == True
    assert strong_number(2) == True
    assert strong_number(7) == False
    assert strong_number(93) == False
    assert strong_number(145) ==  True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
