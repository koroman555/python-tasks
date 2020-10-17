# -*- coding: utf-8 -*-

# Заповнюємо масив випадковоми числами

# Встановити Python Test Explorer for Visual Studio Code
# export PYTHONIOENCODING=utf8 ???

import random
import unittest

def generuvaty_masyv( n, min, max ):
    m = []
    for _ in range(0,n):
            m.append(random.randint(min,max))
    return m

# --- Завдання ---

# Задано масив A
# Ствроити масив В з елементів масиву A які не повторюються

# --- Розвязок ---

def опрацювати_масив(A):
    N = len(A)
    B = []
    for j in range(0,N):
        kilkist = 0
        x = A[j]
        for i in range(0,N):
            if x == A[i]: 
                kilkist = kilkist + 1 
        if kilkist == 1:
            B.append(A[j])
    return B

# --- Перевірка ---

class ТестуватиМасив(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            опрацювати_масив([1,2,3]),
            [1,2,3]
        )

    def test2(self):
        self.assertEqual(
            опрацювати_масив([1,1,1]),
            []
        )

    def test3(self):
        self.assertEqual(
            опрацювати_масив([1,2,1,2,5,2,7]),
            [5,7]
        )

    def test4(self):
        self.assertEqual(
            опрацювати_масив([2,2,1,3,4,3,7]),
            [1,4,7]
        )

if __name__ == '__main__':
    N = 10
    masyv = generuvaty_masyv(N,1,10)
    print("Заданий масив:", masyv)
    print("Результуючий масив:",опрацювати_масив(masyv))
    unittest.main()
