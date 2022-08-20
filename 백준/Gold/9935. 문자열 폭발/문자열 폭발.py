s=input()
a=input()
l = len(a)
ss = []
for i in s:
    ss.append(i)
    if len(ss)>=l:
        if ss[-l:] == list(a):
            for i in range(l):
                ss.pop()
if ss:
    print(''.join(ss))
else:
    print("FRULA")