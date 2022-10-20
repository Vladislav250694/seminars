# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random
number = int (input('Введи любое число: '))
some_list =[]
for i in range (-number,number):
    some_list.append(i)
    random.shuffle (some_list)
print (some_list)
sum = 0
for k in range(len(some_list)):
    if k%2==1:
        sum+=some_list[k]
    else:
        continue
print (sum)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

some_list1 = []
number1 = int (input('Введи любое число: '))
for _ in range (number1):
    nums = int(input())
    some_list1.append(nums)
some_list3 =[]
for indx in range ((number1-1)//2+1):
    number2 = some_list1[indx]
    number3 = some_list1[number1-indx-1]
    some_list3.append(number3 * number2)
print (some_list3)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Алгоритм
num = int(input("Введите число: "))
two_str = ''
while num != 0:
    two_str = str(num%2) + two_str
    num //=2
print(two_str)

# # #Метод
num1 = int(input("Введите число: "))
print (bin(num1))


# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
some_list3 = [0.15, 0.52, 2.95, 3.11,5]
print(some_list3)
some_list4 = []
sum = 0
for i in range(len(some_list3)):
    if ('.') in str(some_list3[i]):
        a = str(some_list3[i]).split('.')[1]
        some_list4.append(a)
    else:
        continue
print (some_list4)
array = list(map(int, some_list4))
print(array)
print(f'0.{max(array) - min(array)}')
