
# Заповнюємо масив випадковоми числами

import random

def generuvaty_masyv( n, min, max ):
    m = []
    for _ in range(0,n):
            m.append(random.randint(min,max))
    return m

N = 20
masyv = generuvaty_masyv( N, 0, 10 )
print("Заданий масив:", masyv)

# знвйдіть елементи більші за суму двох крайніх елементів масиву
#  
