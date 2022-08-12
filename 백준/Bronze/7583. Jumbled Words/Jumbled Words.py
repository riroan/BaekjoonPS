while True:
    s=input()
    if s == '#':
        break
    arr= s.split()
    ans = []
    for i in arr:
        if len(i)<=2:
            ans.append(i)
        else:
            ans.append(i[0]+i[1:-1][::-1]+i[-1])
    print(*ans)