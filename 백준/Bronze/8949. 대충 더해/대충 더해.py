a,b=input().split()
if len(a) < len(b):
    a,b=b,a
ans = []
for i in range(len(b)):
    ans.append(int(a[-1-i])+int(b[-1-i]))
for i in range(len(a) - len(b)):
    ans.append(int(a[-len(b)-i-1]))
ans = ans[::-1]
print(''.join(list(map(str, ans))))