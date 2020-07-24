# Завдання 1003
# Заповнити масив послідовними непарними числами починаючи з одиниці.

masyv = []
N = 10
x = 1

for i in range(0,N):
    masyv.append(x)
    x = x + 3

print(masyv)


