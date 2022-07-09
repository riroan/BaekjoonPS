a, b = map(int, input().split())


def f(n):
    ret = (n+1)//2
    t = 2
    while t <= n:
        ret+=n//t*max(t//2, 2)
        t*=2
    return ret


print(f(b)-f(a-1))
