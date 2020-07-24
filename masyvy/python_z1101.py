
# Заповнюємо масив випадковоми числами

import random

def generuvaty_masyv( N, min, max ):
    m = []
    for _ in range(0,N):
            m.append(random.randint(min,max))
    return m

N = 10
masyv = generuvaty_masyv( N, 5, 15 )
print("Заданий масив:", masyv)

# Знайти кількість парних чисел
