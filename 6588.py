#골드바흐의 추측
#수학, 정수론, 소수 판정, 에라토스테네스의 체

def chae(limit):    #에라토스테네스의 체..
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False
                
    return [x for x in range(2, limit + 1) if primes[x]]

def sosu(n, primes):    #숫자 n까지 소수의 목록 
    if n == 1:
        return False
    
    return n in primes

while True:
    n = int(input())
    if n == 0:
        break
    
    primes = chae(n)
    
    for i in range(2, n):
        if sosu(i, primes) and sosu(n - i, primes):
            print(f'{n} = {i} + {n - i}')
            break
