# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

N = int(input('Введите число N '))
a=[]
b = []
for i in range(N):
    a.append(input())
print (a)

for i in range(N):
    if a[i] not in b:
        b.append(a[i])
print (b)