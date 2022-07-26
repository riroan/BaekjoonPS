n = 1000010
sieve = [1]*n
sieve[0] = sieve[1] = 0
for i in range(2, n):
    if sieve[i] == 0:
        continue
    for j in range(2*i, n, i):
        sieve[j] = 0
primes = [1]
for i, v in enumerate(sieve):
    if v:
        primes.append(i)


n = int(input())
arr = [int(input()) for i in range(n)]
dd = [0]*1000010
for i in arr:
    dd[i] += 1
ans = [0]*1000010
for ix, i in enumerate(arr):
    for j in range(1, int(i**0.5)+1):
        if i == 1 and j == 1 and ans[ix] == 0:
            ans[ix] += dd[1]-1
        elif i%j == 0:
            a, b = j, i//j
            ans[ix] += dd[a]
            if a!=b:
                if j==1:
                    ans[ix] += dd[b]-1
                else:
                    ans[ix] += dd[b]
for i in range(n):
    print(ans[i])
