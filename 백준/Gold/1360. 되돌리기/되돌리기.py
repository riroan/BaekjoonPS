d = {}
sec = []
current = ''
for _ in range(int(input())):
    s = input().split()
    if s[0] == 'type':
        b = s[1]
        c = int(s[2])
        sec.append(c)
        current += b
        d[c] = current
    elif s[0] == 'undo':
        b, c = map(int, s[1:])
        sec.append(c)
        for i in range(len(sec)-1,-1,-1):
            if sec[i] <c-b:
                current = d[sec[i]]
                break
        else:
            current = ''
        d[c] = current
print(current)
