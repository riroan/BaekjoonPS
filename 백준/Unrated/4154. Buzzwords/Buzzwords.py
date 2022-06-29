from collections import defaultdict
arr = []
try:
    while True:
        arr.append(input())
except:
    pass
for s in arr:
    s = s.replace(" ", "")
    for i in range(1, len(s)):
        dd = defaultdict(int)
        for j in range(len(s) - i+1):
            dd[s[j:j+i]] += 1
        m = max(dd.values())
        if m > 1:
            print(m)
    print()
