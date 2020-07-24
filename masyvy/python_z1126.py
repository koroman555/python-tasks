
# Заповнюємо масив випадковоми числами

import random

def generuvaty_masyv( n, min, max ):
    m = []
    for _ in range(0,n):
            m.append(random.randint(min,max))
    return m

N = 20
masyv = generuvaty_masyv( N, -10, 10 )
print("Заданий масив:", masyv)

# визначте скільки раз змінюється знак елементів масиву
# приклад:
# [-1, -4, 10, 9, -4, 3, 7, 9, -8, -1]
# відповідь 4
