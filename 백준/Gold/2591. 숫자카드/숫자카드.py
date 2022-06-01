s = input()
n = len(s)
a = s[:n//2]
b = s[n//2:]
cnt = [0, 0, 0, 0, 0, 0]
na, nb = len(a), len(b)
flag = True
for i in range(n):
    if s[i] == '0':
        if i == 0:
            flag = False
        else:
            if s[i-1] not in '123':
                flag = False


def f(s, ix):
    global cnt
    if ix >= len(s):
        cnt[u] += 1
        return
    if s[ix]!='0':
        f(s, ix+1)
        if ix < len(s)-1:
            if int(s[ix:ix+2]) <= 34:
                f(s, ix+2)


if not flag:
    print(0)
else:
    if len(s) <= 20:
        u = 0
        f(s, 0)
        print(cnt[0])
    else:
        u = 0
        f(a, 0)
        u = 1
        f(b, 0)
        if int(a[-1]+b[0]) <= 34 and a[-1] != '0':
            u = 4
            f(a[:-1], 0)
            u = 5
            f(b[1:], 0)
            print(cnt[0]*cnt[1]+cnt[4]*cnt[5])
        else:
            print(cnt[0]*cnt[1])
