# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
#  Пример:
#  k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
polynome=''
k = int(input('Введите k '))
coefs_arr = [random.randint(0,10) for i in range(k)]
print(coefs_arr)
for i in range(k):
    if coefs_arr[i]!=0:
        if i==k-1:
            polynome+=str(coefs_arr[i])+"x^"+str(k-i)
        else:
            polynome+=str(coefs_arr[i])+"x^"+str(k-i)+" + "
c = random.randint(0,10)
if c!=0:
    polynome+=" + "+str(c)+" = 0"
print(polynome)

with open('file_polindrom.txt', 'w',encoding='utf-8') as data:
    data.write(polynome)