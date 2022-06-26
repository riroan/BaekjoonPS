for _ in range(int(input())):
    s = input().lower()
    ok = True
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            ok = False
    if ok:
        print("Yes")
    else:
        print("No")