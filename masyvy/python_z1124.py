
# Заповнюємо масив випадковоми числами

import random

def generuvaty_masyv( n, min, max ):
    m = []
    for _ in range(0,n):
            m.append(random.randint(min,max))
    return m

N = 20
masyv = generuvaty_masyv( N, 1, 30 )
print("Заданий масив:", masyv)

# Створити три нові масиви з елементів заданого масиву:
# Перший з елементів < 10
# Другий з елементів 10 <= x <= 20
# Третій з елементів > 20
