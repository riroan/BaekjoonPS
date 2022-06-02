n,m = map(int, input().split())
def func(n,u):
    ret = 0
    k = u
    while k <= n:
        ret+=n//k
        k*=u
    return ret
print(min(func(n,5)-func(m,5)-func(n-m,5),func(n,2)-func(m,2)-func(n-m,2)))