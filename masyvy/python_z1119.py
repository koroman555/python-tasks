
# Заповнюємо масив випадковоми числами

import random

def generuvaty_masyv( n, min, max ):
    m = []
    for _ in range(0,n):
            m.append(random.randint(min,max))
    return m

N = 20
A = generuvaty_masyv( N, 1, 20 )
print("Заданий масив:", A)

# Створіть новий масив B кожен елемент якого є сумою елементу
# масиву A який стоїть на тому ж місці та наступного за ним.
# B[i] = A[i] + A[i+1]
