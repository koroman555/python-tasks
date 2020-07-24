
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

# Задача (викладка з легендою)
# В черзі на завантаження на корабель стоять 20 контейнерів.
# Вага кожного контейнера є в масиві (від 1 до 20 тон). Порядок елементів і є чергою
# нульовий контейнер треба брати першим, а за ним послідовно решту.
# Корабель може взяти на борт 50 тон контейнерів за один рейс.
# Потребіно перевезти усі контейнери, навантажуючи корабель 
# контейнерами в порядку черги, але не більше ніж може взяти корабель за рейс.
# Вивести номера контейнерів які йдуть в кожен рейс та
# скільки рейсів потрібно зробити кораблеві щоб
# перевести усі контейнери.

# Задача (технічна викладка)
# Розбити елементи масиву на послідовні групи починаючи з 0-го елементу
# щоб сума значень елементів групи не була більша 50.
# Вивести розподіл елементів по групах та кількість груп.

# ------------- Спрощений вивід без оформлення

reys = 1
suma = 0
print("Рейс:", reys)
for i in range(0,N):

    if (suma + masyv[i]) <= 50:
        # якщо влазить то додаємо до рейсу
        suma = suma + masyv[i]
        print(i)
    else:
        # якщо не влазить додаємо до нового рейсу
        print("Cума:", suma)
        reys = reys + 1
        print("Рейс:", reys)
        suma = masyv[i]
        print(i)
    
    if i==(N-1):
        print("Cума:", suma)
      
print("Всього рейсів:", reys)