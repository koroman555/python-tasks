
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

# Виведіть індекси парних чисел що більше 10
# та індекси непарних що менше 5
