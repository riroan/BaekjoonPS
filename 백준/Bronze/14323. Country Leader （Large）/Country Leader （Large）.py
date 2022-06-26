import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n=int(input())
    arr = [input() for i in range(n)]
    m = 0
    for i in arr:
        s = set(list(i.replace(' ','')))
        m=max(len(s),m )
    ans = []
    for i in arr:
        if len(set(list(i.replace(' ', '')))) == m:
            ans.append(i)
    ans.sort()
    print(f"Case #{test+1}:", end=" ")
    print(ans[0])
    