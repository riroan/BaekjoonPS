ans = ''
while True:
    s = input()
    for i in '0123456789.()[]{},\'\"':
        s=s.replace(i, '')
    for i in s.split():
        if i == 'E-N-D':
            continue
        if len(i) > len(ans):
            ans = i
    if s[-5:] == 'E-N-D':
        break
print(ans.lower())