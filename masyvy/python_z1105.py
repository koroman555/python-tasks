
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

# Знайдіть дві суми:
# Суму парних числел масиву які стоять на парних місцях
# Суму непарних числ які стоять на непарних місцях