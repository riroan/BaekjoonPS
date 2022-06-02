s = set()
for i in range(int(input())):
    ss = list(input())
    ss.sort()
    s.add(tuple(ss))
print(len(s))