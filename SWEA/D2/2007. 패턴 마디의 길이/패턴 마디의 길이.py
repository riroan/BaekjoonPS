
for test in range(int(input())):
    print(f"#{test+1}", end=" ")
    s = input()
    ans = 10**18
    for i in range(1, 11):
        tmp = []
        for j in range(0, len(s), i):
            tmp.append(s[j:min(j+i, len(s))])
        ok = tmp[0] == tmp[1]
        if ok:
            ans = min(ans, i)
            break
    print(ans)