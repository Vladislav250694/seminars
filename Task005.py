# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input ('Введи текст: ')
text = text.split()
new_text = ' '
for i in text:
    if 'abc' not in i:
        new_text += i + ' '
print (new_text)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")

