while 1:
    s=list(input())
    if s == ['#']:
        break
    n= len(s)
    ok = 0
    for i in range(n):
        if s[i] in 'aeiou':
            ok = 1
            break
    if ok:
        a = s[:i]
        b = s[i:]
        print(''.join(b+a)+"ay")
    else:
        print(''.join(s) + 'ay')