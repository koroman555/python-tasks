
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

# Знайти кількість чисел в масиві які діляться на 3
# Та вивести їх
