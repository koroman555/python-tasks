# Приклад 1
# Заповніть масив числами від 1 до 10

masyv = []
start = 1
finish = 10
for i in range(start,finish+1):
    masyv.append(i)

print("Приклад 1:", masyv)

# Приклад 2
# Заповніть масив числами від 10 до 1

masyv = []
start = 10
finish = 1
for i in range(start,finish-1,-1):
    masyv.append(i)

print("Приклад 2:", masyv)

# Приклад 3
# Заповніть масив парними числами

masyv = []
N = 10
for i in range(1,N+1):
    masyv.append(i*2)

print("Приклад 3:", masyv)

# Приклад 4
# Заповніть масив квадратами чисел від 4 до 10

masyv = []
s = 4
f = 10
for i in range(4,f+1):
    masyv.append(i*i)

print("Приклад 4:", masyv)
