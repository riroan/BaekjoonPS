for _ in range(3):
    s=list(map(int, list(input())))
    start = 0
    ans = 0
    for i in range(8):
        if s[i] != s[start]:
            ans = max(ans, i-start)
            start = i
    ans = max(ans ,8-start)
    print(ans)
    
