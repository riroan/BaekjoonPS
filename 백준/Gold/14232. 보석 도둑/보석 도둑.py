def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n = 2000000
sieve = [1]*n
sieve[0] = sieve[1] = 0
for i in range(2, n):
    if sieve[i] == 0:
        continue
    for j in range(2*i,n,i):
        sieve[j] = 0
primes = []
for i, v in enumerate(sieve):
    if v:
        primes.append(i)
ss = set(primes)
n=int(input())
if isPrime(n):
    print(1)
    print(n)
else:
    arr = []
    for i in primes:
        while n%i==0:
            n//=i
            arr.append(i)
    if n>1:
        arr.append(n)
    arr.sort()
    print(len(arr))
    print(*arr)