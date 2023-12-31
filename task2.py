# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды 
# с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Количество кустов: '))
berry = []
max = 0
sum_berry = 0
for i in range (n):
    print(f'Количество ягод на {i + 1} кусте: ')
    berry_num = int(input())
    berry.append(berry_num)
print(berry)

for i in range (len(berry)):
    if n <= 3:
        sum_berry += berry[i]
    elif i + 1 >= len(berry):
        sum_berry = berry[i - 1] + berry[i] + berry[0]
    else:
        sum_berry = berry[i - 1] + berry[i] + berry[i + 1]
    if max < sum_berry:
        max = sum_berry
print(max)