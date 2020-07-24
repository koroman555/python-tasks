
# Заповнюємо масив випадковоми числами

import random

def generuvaty_masyv( n, min, max ):
    m = []
    for _ in range(0,n):
            m.append(random.randint(min,max))
    return m

N = 10
masyv = generuvaty_masyv( N, 5, 15 )
print("Заданий масив:", masyv)

# Приклад 1
# Знайти кількість елементів більші за 10

kilkist = 0
for i in range(0,N):
    if masyv[i] > 10:
        kilkist = kilkist + 1

print("Кількість:", kilkist)

# Приклад 2
# Знайти суму елементів менших-рівних за 10

suma = 0
for i in range(0,N):
    if masyv[i] <= 10:
        suma = suma + masyv[i]

print("Cума:", suma)
