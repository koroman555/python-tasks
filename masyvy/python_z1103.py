
# Заповнюємо масив випадковоми числами

import random

def generuvaty_masyv( n, min, max ):
    m = []
    for i in range(0,n):
            m.append(random.randint(min,max))
    return m

N = 20
masyv = generuvaty_masyv( N, 1, 20 )
print("Заданий масив:", masyv)

# Визначити кількіть елементів які діляться на 5
# Визначити кількіть елементів які діляться на 3
