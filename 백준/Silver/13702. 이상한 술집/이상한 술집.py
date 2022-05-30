n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]


def check(x):
    s = 0
    for i in arr:
        s += i//x
    return s


l = 0
r = 2**32
while l + 1 < r:
    mid = (l+r)//2
    k = check(mid)
    if k >= m:
        l = mid
    else:
        r = mid
while check(mid) < m:
    mid -= 1
print(mid)