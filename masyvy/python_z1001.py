# Завдання 1001
# Заповніть масив нулями, крім першого та останнього елементів,
# які мають бути рівні одиниці.

masyv = []
N = 10
for i in range(N):
    if i == 2 or i == (N-2):
        masyv.append(1)
    else:
        masyv.append(0)
print(masyv)
