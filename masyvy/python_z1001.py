# Завдання 1001
# Заповніть масив нулями, крім першого та останнього елементів,
# які мають бути рівні одиниці.

masyv = []
N = 10
for i in range(N):
    if i == 0 or i == (N-1):
        masyv.append(1)
    else:
        masyv.append(0)
print(masyv)
