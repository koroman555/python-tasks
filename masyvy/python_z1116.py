
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

# Найдіть кількість елементів масиву які менші за максимальний не більше як на 5,
# виведіть їх значення
