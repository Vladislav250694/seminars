# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input('Введи число: ')
sum = 0
for i in number:
    if i != '.' and i != ' ' and i!= '-':
        sum += int(i)
print (sum)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
import math
number1 = int (input('Введите число: '))
any_list = [ ]
for i in range (1, number1+1):
    any_list.append (math.factorial(i))
print (any_list)


# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
number2 = int (input('Введите число: '))
sum = 0
for i in range (1, number2+1):
    sum+= round((1+(1/i))**i,2)
print (sum)


