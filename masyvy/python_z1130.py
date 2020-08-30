
# Заповнюємо масив випадковоми числами

import random

def generuvaty_masyv( n, min, max ):
    m = []
    for _ in range(0,n):
            m.append(random.randint(min,max))
    return m

N = 20
masyv = generuvaty_masyv( N, 0, 1 )
print("Заданий масив:", masyv)

# Задано масив з елементів 0 та 1
# Визначте скільки раз змінюються нулі на одиниці та навпаки
# Приклади:
# [0, 0, 0, 1, 1, 1, 0, 0, 0]
# відповідь: 2
# [1, 1, 0, 1, 1, 1, 0, 0, 1]
# відповідь: 4
# [1, 1, 1]
# відповідь: 0