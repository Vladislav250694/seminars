# Вычислить число c заданной точностью d
num = float(input('Число '))
t = float(input('округление  '))
if t == 1:
    print (int(num))
else:
    t = str(t).split('.')[1]
    t=len(t)
    print (round (num, t))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = int(input('Введи '))
list_1 = []
for i in range (2,number+1):
    if number%i ==0:
        for j in range (2,i//2+1):
            if i%j==0:
                break
        else:
            list_1.append(i)
print(list_1)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
k = [3, 4, 5, 6, 4, 2,5,3,1,15,21,15]
b = []
for i in k:
    if k.count(i) == 1:
        b.append(i)
print(b)

#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
some_dict = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
k = int(input('Введите натуральную степень k: '))
coef = [random.randint(0, 100) for _ in range(k + 1)]
print(coef)
with open('coef.txt', 'w', encoding='utf-8') as m:
    for i in range(len(coef)):
        if k - i != 1 and k - i != 0:
            m.write(f'{coef[i]}x{some_dict[k - i]} + ')
        elif k - i == 1:
            m.write(f'{coef[i]}x + ')
        elif k - i == 0:
            m.write(f'{coef[i]} = 0')