# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int (input ('Введите любую цифру соответствующая дню недели: '))
if day in range (1,8):
    if day in range (1,6):
        print ('Это рабочий день')
    else:
        print('Это не рабочий день')
else:
    print('Вы ввели не правильную цирфу/число')


# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in (0,1):
    for y in (0,1):
        for z in (0,1):
            print ((not(x or y or z)) == (not x and not y and not z))

# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x1 = int (input ('Введите координату Х: '))
y1 = int (input ('Введите координату Y: '))
if x1 >0 and y1 >0:
    print ('перая четверть')
elif x1 < 0 and y1 > 0:
    print('вторая четверть')
elif x1 < 0 and y1 < 0:
    print('третья четверть')
else:
    print('четвертая четверть')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

number = int (input ('Введите номер четверти: '))
if number == 1:
    print ('x>0 и y>0')
elif number == 2:
    print('x<0 и y>0')
elif number == 3:
    print('x<0 и y<0')
elif number == 4:
    print('x>0 и y<0')
else:
    print('Выбран неверный номер четверти')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
x2 = int (input ('Введите координату Х1: '))
y2 = int (input ('Введите координату Y1: '))
x3 = int (input ('Введите координату Х2: '))
y3 = int (input ('Введите координату Y2: '))
bc = x2 - x3
ac = y2 - y3
print ('Расстояние между точками: ', round((ac**2 + bc **2) ** 0.5,2))