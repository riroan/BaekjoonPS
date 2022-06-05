from collections import defaultdict
d = defaultdict(int)
m = 0
for i in range(int(input())):
    s = input()
    d[s]+=1
    m = max(d[s],m)
for i in sorted(d):
    if d[i] == m:
        print(i)
        break