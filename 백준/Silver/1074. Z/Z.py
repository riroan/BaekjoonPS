n, row, col = map(int, input().split())


def solve(l, r, u, d, cur = 0):
    if r-l == 1 and d-u == 1:
        print(cur)
        return
    m = (l+r)//2
    mm = (u+d)//2
    ne = 0
    if m <= col < r:
        ne |= 1
    if mm <= row < d:
        ne |=2
    cur += ((r-l)//2)**2 * ne
    if ne == 0:
        solve(l, m, u, mm, cur)
    if ne == 1:
        solve(m, r, u, mm, cur)
    if ne == 2:
        solve(l, m, mm, d, cur)
    if ne == 3:
        solve(m, r, mm, d, cur)

solve(0,2**n,0,2**n)