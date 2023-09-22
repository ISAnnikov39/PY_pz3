# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
#  Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

n = 10

import random

array= [random.randint(0,20) for i in range(n) ]

print(array)

result = []

length = len(array)

sum = array[0] + array[length-1] # чтобы узнать ОБЩУЮ сумму со СМЕЖНЫМИ грядки с 0 и последним индексом

for i in range(length):
    if i==0:
        result.append(sum + array[1]) # грядка с 0 индексом
    elif 0 < i < length-2:
        result.append(array[i] + array[i-1] + array [i+1]) # сумма всех кроме первой и последней грядки
    else:
        result.append(sum + array[length-2]) # с последним индексом

print(max(result))



