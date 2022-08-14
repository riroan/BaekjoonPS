from itertools import permutations
s=input()
number=[]
char=[]
a = []
b= []
for i in range(len(s)):
    if s[i] in '0123456789':
        a.append(s[i])
        number.append(i)
    else:
        b.append(s[i])
        char.append(i)
ss = set()
for i in permutations(a):
    for j in permutations(b):
        ans = ['']*len(s)
        for x,y in zip(i, number):
            ans[y] = x
        for x,y in zip(j, char):
            ans[y] = x
        ss.add(''.join(ans))
print(len(ss))
for i in ss:
    print(i)