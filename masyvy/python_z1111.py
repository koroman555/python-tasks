
# Заповнюємо масив випадковоми числами

import random

def generuvaty_masyv( n, min, max ):
    m = []
    for _ in range(0,n):
            m.append(random.randint(min,max))
    return m

N = 20
masyv = generuvaty_masyv( N, 1, 20 )
print("Заданий масив:", masyv)

# Найдіть номер(індекс) найбільшгого елементу масиву 

maxv = masyv[0]
maxi = 0
for i in range(1,N):
    if masyv[i] > maxv:
       maxv = masyv[i]
       maxi = i
print("Номер максимального елементу:", maxi)

