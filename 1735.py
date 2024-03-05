# 분수 합

import math #gcd - 최대공약수 사용

a,b = map(int, input().split()) #1번 분수
x,y = map(int, input().split()) #2번 분수 

def gcd(a,b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    return b

#최대곻약수 n

n = gcd(a * y + b * x, b * y)
print((a * y + b * x) // n, (b * y) // n)
