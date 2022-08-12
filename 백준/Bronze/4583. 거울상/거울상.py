d = {}
d['b'] = 'd'
d['d'] = 'b'
d['p'] = 'q'
d['q'] = 'p'
for i in 'iovwx':
    d[i] = i
while 1:
    s = input()
    if s =='#':
        break
    try:
        ans = ''
        for i in s:
            ans+=d[i]
        print(ans[::-1])
    except:
        print("INVALID")