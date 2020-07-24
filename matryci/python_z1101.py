# Завдання 1101
# кількість елементів більша 10

import random
from matryciutils import *

def kilkist_bilsha_x( a, n, m, x ):
    kilkist = 0
    for i in range(0,n):
        for j in range(0,m):
            # тут змінна element потірбна лише для демонстрації Debug
            element = a[i][j]
            if element > 10:
                kilkist = kilkist + 1
    return kilkist

matrix = []
N = 5
M = 6
generuvaty_matrycyu( matrix, N, M )
print('-' * 40 )
print('Початкова матриця')
print('-' * 40 )
vyvesty_matrycyu( matrix, N, M )
print('-' * 40 )

k = kilkist_bilsha_x( matrix, N, M, 10 )
print("Кількість: ", k)


