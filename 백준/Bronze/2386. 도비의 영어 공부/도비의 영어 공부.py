while True:
    s = input().lower()
    if s == "#":
        break
    cnt = 0
    for i in s[2:]:
        if i == s[0]:
            cnt+=1
    print(s[0], cnt)