import random

def generuvaty_matrycyu( a, n, m ):
    for _ in range(0,n):
        row = []
        for _ in range(0,m):
            row.append(random.randint(0, 20))
        a.append(row)

def vyvesty_matrycyu(a, n, m):
    for i in range(0,n):
        for j in range(0,m):
            print('{:4d}'.format(a[i][j]), end='')
        print()