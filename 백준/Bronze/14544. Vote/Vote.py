import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n,k=map(int, input().split())
    d = {}
    for i in range(n):
        d[input()] = 0
    for i in range(k):
        a,b,c=input().split()
        b = int(b)
        d[a] += b
    m = max(list(d.values()))
    print(f"VOTE {test+1}: ",end="")
    if list(d.values()).count(m)>=2:
        print("THERE IS A DILEMMA")
    else:
        ans = ""
        for i in d:
            if d[i] == m:
                ans = i
        print(f"THE WINNER IS {ans} {m}")