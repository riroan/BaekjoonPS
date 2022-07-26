n = 1000010
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


n = int(input())
k=n
arr = []
for i in primes:
    while n%i==0:
        arr.append(i)
        n//=i
if n>1:
    arr.append(n)
if len(arr)==1:
    print(-1)
elif len(arr) <= 3:
    print(k)
else:
    brr = []
    for i in range(0, len(arr)-1, 2):
        brr.append(arr[i]*arr[i+1])
    if len(arr)%2:
        brr[-1]*=arr[-1]
    print(*brr)