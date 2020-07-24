# Завдання 1002
# Заповніть масив нулями і одиницями,
# при цьому дані значення розміщуються почергово,
# починаючи з нуля

# Variant 1

masyv = []
N = 10
for i in range(0,N,2):
    masyv.append(1)
    masyv.append(0)
print("Variant 1: ", masyv)

# Variant 2

masyv = []
N = 10
v = 1
for i in range(0,N):
    masyv.append(v)
    if v == 0:
        v = 1
    else:
        v = 0
print("Variant 2: ", masyv)

# Variant 3

masyv = []
N = 10
masyv.append(1)
for i in range(1,N):
    if masyv[i-1] == 0:
        masyv.append(1)
    else:
        masyv.append(0)
print("Variant 3: ", masyv)

# Variant 4

masyv = []
N = 10
masyv.append(1)
for i in range(1,N):
    if (i % 2) == 0:
        masyv.append(1)
    else:
        masyv.append(0)
print("Variant 4: ", masyv)